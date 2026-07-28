# Stream audio from an I2S microphone to a computer over Bluetooth.
#
# The ESP32-S3 acts as a BLE peripheral.  It reads 16 bit samples from an
# INMP441 microphone, shrinks them to 8 bits to save bandwidth, and sends them
# to the connected computer as a stream of BLE notifications.
#
# Run i2s_ble_computer.py on the computer to record and play the audio.

import bluetooth
import micropython
import time
from machine import I2S, Pin
from ble_audio_peripheral import BLEAudioPeripheral
from button import Button


# ---------------------------------------------------------------------------
# Microphone wiring
# ---------------------------------------------------------------------------
SCK_PIN = 14    # Bit clock output
WS_PIN = 13     # Word clock output
SD_PIN = 12     # Serial data input
PTT_PIN = 21    # Push to talk button pin

# ---------------------------------------------------------------------------
# Audio format.  These settings must match the ones in i2s_ble_computer.py
# ---------------------------------------------------------------------------
SAMPLE_RATE = 8000      # Samples per second
SAMPLES_PER_READ = 256  # Samples read from the microphone at a time (32 ms)
GAIN_SHIFT = 1          # Increase to increase gain, 0 is no gain

DEVICE_NAME = "ESP32MIC"


@micropython.native
def down_sample(pcm16, pcm8, count):
    """Turn signed 16 bit samples into the louder, smaller 8 bit samples we send.

    A WAV file stores 8 bit audio as unsigned numbers where 128 is silence, so
    each sample is scaled down, clipped, and then shifted up by 128.
    """
    for i in range(count):
        sample = pcm16[2 * i] | (pcm16[2 * i + 1] << 8)
        if sample > 32767:
            sample -= 65536
        sample >>= 8 - GAIN_SHIFT
        if sample > 127:
            sample = 127
        elif sample < -128:
            sample = -128
        pcm8[i] = sample + 128

IDLE = 0x00
RECORD = 0x01
STOP = 0x02

class PushToStream:
    def __init__(self, sck_pin, ws_pin, sd_pin, push_to_talk_pin, sample_rate, samples_per_read, ble_device_name):
        self._ble = bluetooth.BLE()
        self.peripheral = BLEAudioPeripheral(self._ble, ble_device_name, self.on_command)
        self._audio_in = I2S(0,
            sck=Pin(sck_pin),
            ws=Pin(ws_pin),
            sd=Pin(sd_pin),
            mode=I2S.RX,
            bits=16,
            format=I2S.MONO,
            rate=sample_rate,
            ibuf=samples_per_read * 8,
        )
        self._ptt_button = Button(push_to_talk_pin, self.ptt_callback)
        self.ptt_pressed = False
        self.command = IDLE
        self.buff16 = bytearray(samples_per_read * 2)   # Read from I2S device at 16 bits
        self.buff8 = bytearray(samples_per_read)        # Stream over bluetooth at 8 bits

    def ptt_callback(self):
        print("Button Pressed")
        if not self.ptt_pressed:
            self.command = RECORD
        elif self.ptt_pressed:
            self.command = STOP
        self.ptt_pressed = not self.ptt_pressed
    
    def on_command(self, command):
        if command == b"0":
            self.command = IDLE

    def streaming(self):
        return self.ptt_pressed and self.peripheral.streaming
    
    def read_and_stream(self):
        bytes_read = self._audio_in.readinto(self.buff16)
        count = bytes_read // 2
        down_sample(self.buff16, self.buff8, count)
        self.peripheral.send_audio(self.buff8, count, self.command)

    def deinit(self):
        self._audio_in.deinit()
        self._ble.active(False)   


def demo():
    pttStream = PushToStream(SCK_PIN, WS_PIN, SD_PIN, PTT_PIN, SAMPLE_RATE, SAMPLES_PER_READ, DEVICE_NAME)

    print("Please connect to", DEVICE_NAME)
    reported = time.ticks_ms()

    try:
        while True:
            if not pttStream.streaming:
                time.sleep_ms(1)
                continue

            pttStream.read_and_stream()

            # Print status once a second
            now = time.ticks_ms()
            if time.ticks_diff(now, reported) >= 1000:
                print(f"Dropped packets: {pttStream.peripheral.dropped} Command: {pttStream.command}")
                reported = now
    except KeyboardInterrupt:
        print("Stopping")
    finally:
        pttStream.deinit()


if __name__ == "__main__":
    demo()
