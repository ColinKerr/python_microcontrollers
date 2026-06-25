from machine import Pin
import time

led = Pin(2, Pin.OUT)

#create button object from pin13,Set Pin13 to Input
button = Pin(13, Pin.IN,Pin.PULL_UP) 

try:
    while True:
      if not button.value():     
        led.value(0)  #Set led turn off instead of on.
      else: #LED Blinks until pressed.
        led.value(0)
        time.sleep_ms(500)
        led.value(1)
        time.sleep_ms(500)
except:
    pass
