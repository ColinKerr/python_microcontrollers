# Class PWM(pin, freq)

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) — Chapter 4, Analog & PWM

Before each use of the PWM module, add the statement `from machine import PWM` to the top of the Python file.

- `pin`: Any pin that supports PWM output, except GPIO19 and GPIO20.
- `freq`: Output frequency, with a range of 0–78125 Hz.
- `duty`: Duty cycle, with a range of 0–1023.
- **`PWM.init(freq, duty)`**: Initializes PWM. Parameters are the same as above.
- **`PWM.freq([freq_val])`**: With no parameter, obtains and returns the PWM frequency. With a parameter, sets the PWM frequency and returns nothing.
- **`PWM.duty([duty_val])`**: With no parameter, obtains and returns the PWM duty cycle. With a parameter, sets the PWM duty cycle.
- **`PWM.deinit()`**: Turns PWM off.
