# Class ADC

Before each use of the ADC module, add the statement `from machine import ADC` to the top of the Python file.

- **`machine.ADC(pin)`**: Creates an ADC object associated with the given pin.
  - `pin`: Available pins are Pin(1–18).
- **`ADC.read()`**: Reads the ADC and returns the value.
- **`ADC.atten(db)`**: Sets the attenuation ratio (i.e. the full-range voltage — for example, the voltage at 11db full range is 3.3V).
  - `db`: Attenuation ratio.
    - `ADC.ATTN_0DB` — full range of 1.2V
    - `ADC.ATTN_2_5DB` — full range of 1.5V
    - `ADC.ATTN_6DB` — full range of 2.0V
    - `ADC.ATTN_11DB` — full range of 3.3V
- **`ADC.width(bit)`**: Sets the data width.
  - `bit`: Data bit width.
    - `ADC.WIDTH_9BIT` — 9-bit data width
    - `ADC.WIDTH_10BIT` — 10-bit data width
    - `ADC.WIDTH_11BIT` — 11-bit data width
    - `ADC.WIDTH_12BIT` — 12-bit data width

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) — Chapter 9, AD Converter