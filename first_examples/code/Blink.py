from time import sleep_ms
from machine import Pin

led=Pin(2,Pin.OUT) #create LED object from pin2,Set Pin2 to output

while True:
    led.value(1)    # Turn LED On
    sleep_ms(1000)
    led.value(0)    # Turn LED Off
    sleep_ms(1000)
