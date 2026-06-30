# Class I2cLcd

Before each use of the object **I2cLcd**, make sure `I2C_LCD.py` and `LCD_API.py` have been uploaded to `/` on the ESP32-S3, and then add the statement `from I2C_LCD import I2cLcd` to the top of the Python file.

- **`clear()`**: Clears the LCD1602 screen display.
- **`show_cursor()`**: Shows the cursor.
- **`hide_cursor()`**: Hides the cursor.
- **`blink_cursor_on()`**: Turns on cursor blinking.
- **`blink_cursor_off()`**: Turns off cursor blinking.
- **`display_on()`**: Turns on the LCD1602 display.
- **`display_off()`**: Turns off the LCD1602 display.
- **`backlight_on()`**: Turns on the backlight.
- **`backlight_off()`**: Turns off the backlight.
- **`move_to(cursor_x, cursor_y)`**: Moves the cursor to a specified position.
  - `cursor_x`: Column position.
  - `cursor_y`: Row position.
- **`putchar(char)`**: Prints the given character on the LCD1602.
- **`putstr(string)`**: Prints the given string on the LCD1602.

> Copies of these modules can be found in the `reference_code` directory.

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) — Chapter 20, LCD1602