from machine import Pin
import time

led = Pin(2, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_UP)

counter = 0
last_press_time = time.ticks_ms()

def reverseGPIO():
    if led.value():
        led.value(0)
    else:
        led.value(1)

def button_handler(pin):
    global counter
    global last_press_time
    current_time = time.ticks_ms()
    delta_time = time.ticks_diff(current_time, last_press_time)
    if delta_time > 200:
        counter += 1
        print("Button pressed", counter, "times")
        reverseGPIO()
        last_press_time = current_time
    else:
        print("Skipped bounce")
    
button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)