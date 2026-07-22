# Button On and Off Switch using the button class

This project explores creating your own reusable class making it easier to work with a common circuit.  [Project 5.1](./05_1_buttons_interrupts.md) uses interrupts to take button input, this project retains the same circuit but creates a reusable class that can be used for any button.

## New Concepts

- Creating your own python classes

### Creating your own Class

Previous projects used classes to make it easier to work with external components like the ultrasonic sensor, the 74HC595 shift register and the LCD.  Creating a class for a button reduces the code required to add a button to another project.

What does the button class need?

- The pin number the button will connect to.
- The function that will be called when the button is pressed.

This snippet shows the definition of the class and the 'constructor' function (`__init__`):

```python
class Button:
    def __init__(self, pinNum, callback):
```

> Note: notice that the `__init__` function takes in a third parameter `self`.

This snippet shows a button on pin 13 being created.  

```python
button = Button(13, reverseGPIO)
```

> `Button(13, reverseGPIO)` 'constructs' a Button object.  Doing so calls the `__init__` function.  Notice that the constructor takes in two parameters, but the `__init__` function takes in three.  The `self` parameter is not present, it's function will be explained next.


This snippet expands on the `__init__` function.  `self` is used when assigning the input parameters to variables owned by the class.  `self.button = Pin(pinNum, Pin.IN, Pin.PULL_UP)` creates a member variable `button` and creates a new Pin object using the input `pinName`.:

```python
class Button:
    def __init__(self, pinNum, callback):
        self.button = Pin(pinNum, Pin.IN, Pin.PULL_UP)
        self.callback = callback
```

> NOTE: Any function defined in this class must take `self` as the first parameter to be able to access member variables.  Access to member variables must always start with `self.` followed by the member variable name.

## Component List & Circuit

**This project uses the same components and circuit as [Project 5.1](./05_1_buttons_interrupts.md)**


## Code

This project uses two files, one for the Button class and one that uses the button class to implement the On/Off light behavior.

**File:** [05_advanced/code/button.py](./code/button.py)

```python
from machine import Pin
import time

class Button:
    def __init__(self, pinNum, callback):
        self.button = Pin(pinNum, Pin.IN, Pin.PULL_UP)
        self.callback = callback
        self.last_press_time = time.ticks_ms()
        self.button.irq(trigger=Pin.IRQ_RISING, handler=self.button_handler)

    def button_handler(self, pin):
        current_time = time.ticks_ms()
        delta_time = time.ticks_diff(current_time, self.last_press_time)
        if delta_time > 200:
            self.callback()
            self.last_press_time = current_time
```

**File:** [05_advanced/code/ButtonAndLed_OnOff_ButtonClass.py](./code/ButtonAndLed_OnOff_ButtonClass.py)

```python
from button import Button
from machine import Pin

led = Pin(2, Pin.OUT)

def reverseGPIO():
    if led.value():
        led.value(0)
    else:
        led.value(1)

button = Button(13, reverseGPIO)
```

## How to Run

### Online
1. Open Thonny → `05_advanced/code/`.
2. Right-click `button.py` → **Upload to /** if they aren't already on the device.
3. Double-click `ButtonAndLed_OnOff_ButtonClass.py`.
4. Click **Run current script**

## Key Concepts

- **Classes**: A combination of data and behavior that is used to encapsulate functionality for reuse and to make code easier to understand.


## Further Exploration

- Modify the `Button` class so debounce time is configurable.