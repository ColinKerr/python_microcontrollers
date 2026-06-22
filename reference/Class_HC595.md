# Class HC595

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) — Chapter 16, 74HC595 & LED Matrix

Before each use of `HC595`, make sure `HC595.py` has been uploaded to `/` on the ESP32-S3, and then add the statement `import HC595` to the top of the Python file.

- **`Chip74HC595()`**: The object used to control the LED matrix. `chip=Chip74HC595()` or `chip=Chip74HC595(15,2,4,5)`.
- **`set_bit_data(data)`**: Writes data to the 74HC595.
- **`clear()`**: Clears the latch data of the 74HC595.
