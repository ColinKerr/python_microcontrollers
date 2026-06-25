from time import sleep_ms
from machine import Pin

led=Pin(2,Pin.OUT) #create LED object from pin2,Set Pin2 to output

while True:
    led.value(1)    # Turn LED On
    sleep_ms(100)   # Can you make the LED blink fast it looks like its always on?
    led.value(0)    # Turn LED Off
    sleep_ms(35)    # You can also try giving them different on/off times!
