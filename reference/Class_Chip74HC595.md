# Class Chip74HC595

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) — Chapter 14, 74HC595 & LED Bar Graph

Before each use of the `Chip74HC595` object, make sure `my74HC595.py` has been uploaded to `/` on the ESP32-S3, and then add the statement `from my74HC595 import Chip74HC595` to the top of the Python file.

- **`Chip74HC595()`**: An object. By default, 74HC595's DS pin is connected to Pin(14) of ESP32-S3, ST_CP pin is connected to Pin(12), and OE pin is connected to Pin(5). To change the pins: `chip=Chip74HC595()` or `chip=Chip74HC595(12,13,14,5)`.
- **`shiftOut(direction, data)`**: Writes data to the 74HC595.
  - `direction`: `1`/`0`. `1` means the high-order byte is sent first; `0` means the low-order byte is sent first.
  - `data`: The one-byte content to send.
- **`clear()`**: Clears the latch data of the 74HC595.
