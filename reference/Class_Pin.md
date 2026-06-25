# Class Pin(id[, mode, pull, value])

Before each use of the Pin module, please add the statement `from machine import Pin` to the top of thepython file.

- id: Arbitrary pin number
- mode: Mode of pins
  - Pin.IN: Input Mode
  - Pin.OUT: Output Mode
  - Pin.OPEN_DRAIN: Open-drain Mode
- Pull: Whether to enable the internal pull up and down mode
  - None: No pull up or pull down resistors
  - Pin.PULL_UP: Pull-up Mode, outputting high level by default
  - Pin.PULL_DOWN: Pull-down Mode, outputting low level by default
- Value: State of the pin level, 0/1
- Pin.init(mode, pull): Initialize pins
- Pin.value([value]): Obtain or set state of the pin level, return 0 or 1 according to the logic level of pins.  Without parameter, it reads input level. With parameter given, it is to set output level.
  - value: It can be either True/False or 1/0.
- Pin.irq(trigger, handler): Configures an interrupt handler to be called when the pin level meets a condition.
  - trigger:
    - Pin.IRQ_FALLING: interrupt on falling edge
    - Pin.IRQ_RISING: interrupt on rising edge
    - 3: interrupt on both edges
  - handler: callback function