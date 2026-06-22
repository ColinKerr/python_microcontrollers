# Class irrecvdata

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) — Chapter 23, Infrared Remote

Before each use of the object **irrecvdata**, add the statement `from irrecvdata import irGetCMD` to the top of the Python file.

- **`irGetCMD()`**: Object for the infrared decoder, associated with Pin(21) by default.
- **`ir_read()`**: Reads the key value of the infrared remote. Returns the value when read; returns `None` when no value is obtained.
