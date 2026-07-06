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