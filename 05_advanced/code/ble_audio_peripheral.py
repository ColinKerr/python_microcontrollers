from ble_peripheral import BLEBasePeripheral

"""
Streams packets over bluetooth with the format:
[sequence byte][command byte][audio bytes]
"""
class BLEAudioPeripheral(BLEBasePeripheral):
    def __init__(self, ble, name, on_command=None):
        BLEBasePeripheral.__init__(self, ble, name)
        self.streaming = False
        self.dropped = 0
        self._on_command = on_command
        self.on_write(self.on_command)
    
    def on_command(self, command):
        if self._on_command:
            self._on_command(command)

        if command == b"1":
            print("Streaming started")
            self.dropped = 0
            self.streaming = True
        elif command == b"0":
            print("Streaming stopped")
            self.streaming = False

    def send_audio(self, samples, count, command=0):
        chunk = self.max_bytes() - 1 # one byte is used for command
        start = 0
        while start < count:
            end = min(start + chunk, count)
            packet = bytes([command]) + bytes(memoryview(samples)[start:end])
            try:
                self.send(packet)
            except:
                self.dropped += 1
            start = end