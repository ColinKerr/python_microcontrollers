from button import Button
from machine import Pin

led = Pin(2, Pin.OUT)

def reverseGPIO():
    if led.value():
        led.value(0)
    else:
        led.value(1)

button = Button(13, reverseGPIO)