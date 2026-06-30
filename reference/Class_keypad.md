# Class keypad

Before each use of the object **KeyPad**, make sure `keypad.py` has been uploaded to `/` on the ESP32-S3, and then add the statement `from keypad import KeyPad` to the top of the Python file.

- **`KeyPad(row1, row2, row3, row4, col1, col2, col3, col4)`**: Initializes the keypad module and associates its pins with the ESP32-S3.
- **`scan()`**: Non-blocking keypad scan function. If no key is pressed, returns `None`; otherwise, returns the value of the pressed key.

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) — Chapter 22, Matrix Keypad