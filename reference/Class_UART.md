# Class UART

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) — Chapter 8, Serial Communication

Before each use of the UART module, add the statement `from machine import UART` to the top of the Python file.

ESP32-S3 has 3 serial ports. One is used as REPL — Pin(43) and Pin(44) are occupied — and is generally not recommended for use as tx/rx. The other two serial ports can be configured simply by calling the UART module.

- **`UART(id, baudrate, bits, parity, rx, tx, stop, timeout)`**: Defines a serial port and configures its parameters.
  - `id`: Serial number. Available serial port numbers are 1 or 2.
  - `baudrate`: Baud rate.
  - `bits`: The number of bits per character.
  - `parity`: Even or odd check, with 0 for even checking and 1 for odd checking.
  - `rx`, `tx`: UART's reading and writing pins. Note: Pin(1) and Pin(3) are occupied and not recommended for use as tx/rx.
  - `stop`: The number of stop bits — 1 or 2.
  - `timeout`: Timeout period (unit: millisecond). `0 < timeout ≤ 0x7FFFFFFF` (decimal: `0 < timeout ≤ 2147483647`).
- **`UART.init(baudrate, bits, parity, stop, tx, rx, rts, cts)`**: Initializes the serial port.
  - `tx`: Writing pin of UART.
  - `rx`: Reading pin of UART.
  - `rts`: RTS pin of UART.
  - `cts`: CTS pin of UART.
- **`UART.read(nbytes)`**: Reads `nbytes` bytes.
- **`UART.read()`**: Reads data.
- **`UART.write(buf)`**: Writes a byte buffer to the UART bus.
- **`UART.readline()`**: Reads a line of data, ending with a newline character.
- **`UART.readinto(buf)`**: Reads data into a buffer.
- **`UART.readinto(buf, nbytes)`**: Reads data into a buffer, up to `nbytes`.
- **`UART.any()`**: Determines whether there is data in the serial port. If yes, returns the number of bytes; otherwise, returns 0.
