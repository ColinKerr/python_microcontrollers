# Class machine

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) — Chapter 1, LED (Important)

Before each use of the `machine` module, add `import machine` to the top of the Python file.

- **`machine.freq(freq_val)`**: When `freq_val` is not specified, returns the current CPU frequency; otherwise sets the CPU frequency.
  - `freq_val`: `80000000` (80MHz), `160000000` (160MHz), `240000000` (240MHz)
- **`machine.reset()`**: A reset function. When called, the program resets.
- **`machine.unique_id()`**: Obtains the MAC address of the device.
- **`machine.idle()`**: Turns off any temporarily unused functions on the chip and its clock, which is useful for reducing power consumption during short or long periods.
- **`machine.disable_irq()`**: Disables interrupt requests and returns the previous IRQ state. Must be used together with `enable_irq()` — otherwise the machine will crash and restart.
- **`machine.enable_irq(state)`**: Re-enables interrupt requests. The parameter `state` should be the value returned from the most recent call to `disable_irq()`.
- **`machine.time_pulse_us(pin, pulse_level, timeout_us=1000000)`**: Tests the duration of the external pulse level on the given pin and returns the duration in microseconds.
  - When `pulse_level = 1`, it tests the high level duration; when `pulse_level = 0`, it tests the low level duration.
  - If the setting level is not consistent with the current pulse level, it waits until they are consistent, then starts timing. If the set level already matches the current pulse level, it starts timing immediately.
  - When the pin level is opposite to the set level, it waits for timeout and returns `-2`. When the pin level matches the set level, it also waits for timeout but returns `-1`.
  - `timeout_us` is the duration of the timeout.
