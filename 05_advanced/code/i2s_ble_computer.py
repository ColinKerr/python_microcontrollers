# Receive the audio streamed by i2s_ble_micro.py and save it to a WAV file.
#
# Run this on a Mac (or any computer with Bluetooth) while the ESP32-S3 is
# running i2s_ble_micro.py:
#
#     pip install bleak
#     python i2s_ble_computer.py recording.wav
#
# Press Ctrl-C to stop recording.

import asyncio
import signal
import sys
import threading
import wave
import os

from bleak import BleakScanner, BleakClient

DEVICE_NAME = "ESP32MIC"

UART_TX_CHAR_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"  # ESP32 -> computer
UART_RX_CHAR_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"  # computer -> ESP32

# These must match the audio settings in i2s_ble_micro.py.
SAMPLE_RATE = 8000
SAMPLE_WIDTH = 1  # Bytes per sample
SILENCE = 0x80  # 8 bit audio uses 128 for silence, not 0

FOLDER_PATH = "./"


IDLE = 0x00
RECORD = 0x01
STOP = 0x02


async def find_device():
    print(f"Looking for {DEVICE_NAME}...")
    device = await BleakScanner.find_device_by_name(DEVICE_NAME, timeout=15.0)
    if device is None:
        print(f"Could not find a device named {DEVICE_NAME}.")
        print("Check that the ESP32-S3 is powered on and running i2s_ble_micro.py.")
    return device


async def report_progress(recorder):
    """Print how the stream is doing once a second."""
    last_bytes = 0
    while True:
        await asyncio.sleep(1.0)
        rate = (recorder.audio_bytes - last_bytes) / 1024
        last_bytes = recorder.audio_bytes
        print(
            f"\rRecorded {recorder.seconds_recorded():6.1f} s "
            f"| {rate:4.1f} KB/s | lost {recorder.lost_packets} packets | Command: {recorder.command}",
            end="",
            flush=True,
        )

"""
Read a stream of bytes in the format [sequence byte][command byte][payload bytes]
"""
class StreamReader:
    def __init__(self, command_handler, packet_handler=None):
        self._command_handler = command_handler
        self._packet_handler = packet_handler
        self.packets = 0
    
    def handle_packet(self, _characteristic, packet):
        if len(packet) < 3:
            return
        command, payload_bytes = packet[0], packet[1:]
        self.packets += 1

        self._command_handler(command)

        if self._packet_handler:
            self._packet_handler(command, payload_bytes)

    def set_packet_handler(self, packet_handler):
        self._packet_handler = packet_handler

"""
Writes payload bytes to disk using the wav object it was constructed with
"""
class WaveWriter:
    def __init__(self, wav):
        self._wav = wav
        self.audio_bytes = 0
        self.lost_packets = 0
        self.packets = 0
        self._chuck_size = 0

    def audio_packet_handler(self, command, payload_bytes):
        if command != RECORD:
            return
        
        self.audio_bytes += len(payload_bytes)
        self._chunk_size = len(payload_bytes)
        self.packets += 1

        self._write(payload_bytes)

    def _write(self, audio_bytes):
        self._wav.writeframes(audio_bytes)

    def seconds_recorded(self):
        return self._wav.getnframes() / self._wav.getframerate()

"""
Coordinates streaming audio bytes over bluetooth and saving to disk based on button presses by the user
"""
class AudioStreamer:
    def __init__(self, device, sample_width, sample_rate, directory_path):
        self._device = device
        self._sample_width = sample_width
        self._sample_rate = sample_rate
        self._directory_path = directory_path
        self.command = IDLE
        self.stop_event = asyncio.Event()
        self.running = True

    def set_running(self):
        print("Running to false")
        self.running = False

    async def start_streaming(self):
        try:
            loop = asyncio.get_running_loop()
            try:
                loop.add_signal_handler(signal.SIGINT, self.set_running)
            except NotImplementedError:
                pass  # Not supported on Windows;

            await self._stream_audio()
        finally:
            try:
                loop.remove_signal_handler(signal.SIGINT)
            except NotImplementedError:
                pass

    async def _stream_audio(self):
        async with BleakClient(self._device) as client:
            print(f"Connected to {DEVICE_NAME} (packet size {client.mtu_size} bytes)")
            stream_reader = StreamReader(self.handle_command)
            await client.start_notify(UART_TX_CHAR_UUID.lower(), stream_reader.handle_packet)
            print("Stream Reader Created")
            recording_num = 0
            while self.running and recording_num < 100:
                if self.command != RECORD:
                    await asyncio.sleep(0.001)
                    continue

                file_path = os.path.join(self._directory_path, f"recording{recording_num}.wav")
                recording_num += 1
                with wave.open(file_path, "wb") as wav:
                    print("Recording to:", file_path)
                    wav.setnchannels(1)
                    wav.setsampwidth(self._sample_width)
                    wav.setframerate(self._sample_rate)

                    wave_writer = WaveWriter(wav)
                    stream_reader.set_packet_handler(wave_writer.audio_packet_handler)
                    await client.write_gatt_char(UART_RX_CHAR_UUID, b"1", response=False)

                    progress = asyncio.create_task(report_progress(wave_writer))

                    try:
                        self.stop_event.clear()
                        await self.stop_event.wait()
                    finally:
                        stream_reader.set_packet_handler(None)
                        progress.cancel()
                        if client.is_connected:
                            await client.write_gatt_char(
                                UART_RX_CHAR_UUID, b"0", response=False
                            )


                    print(
                        f"\nSaved {wave_writer.seconds_recorded():.1f} seconds to {file_path} "
                        f"({wave_writer.packets} packets, {wave_writer.lost_packets} lost)"
                    )
            await client.stop_notify(UART_TX_CHAR_UUID)

    
    def handle_command(self, command):
        self.command = command
        if (self.command == STOP):
            self.stop_event.set()

async def main():

    device = await find_device()
    if device is None:
        return

    streamer = AudioStreamer(device, SAMPLE_WIDTH, SAMPLE_RATE, FOLDER_PATH)
    await streamer.start_streaming()
    print("Finished stream_audio")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopped.")
