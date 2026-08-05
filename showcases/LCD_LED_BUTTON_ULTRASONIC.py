import time
from machine import Pin, I2C
from I2C_LCD import I2cLcd

# BUTTON SETUP (toggle)
button = Pin(4, Pin.IN, Pin.PULL_UP)
system_on = False     # starts OFF
last_state = 1        # used for debouncing


# LED SETUP
led = Pin(2, Pin.OUT)
led.value(0)   # LED OFF at start

# ULTRASONIC SETUP
trig = Pin(5, Pin.OUT)
echo = Pin(18, Pin.IN)
sound_speed = 340

def get_distance():
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    while echo.value() == 0:
        pass
    start = time.ticks_us()

    while echo.value() == 1:
        pass
    end = time.ticks_us()

    duration = time.ticks_diff(end, start)
    return (duration * sound_speed) // 2 // 10000

# LCD SETUP
i2c = I2C(scl=Pin(13), sda=Pin(14), freq=400000)
devices = i2c.scan()

if len(devices) == 0:
    print("No I2C LCD found!")
    while True:
        pass

lcd_addr = devices[0]
lcd = I2cLcd(i2c, lcd_addr, 2, 16)

lcd.clear()
lcd.putstr("Press button")

# MAIN LOOP

while True:

    # BUTTON TOGGLE LOGIC
  
    current = button.value()

    if current == 0 and last_state == 1:   # button pressed
        system_on = not system_on          # toggle ON/OFF
        time.sleep_ms(20)                  # debounce

        if system_on:
            led.value(1)                   # LED ON
            lcd.clear()
            lcd.putstr("Ultrasonic ON")
        else:
            led.value(0)                   # LED OFF
            lcd.clear()
            lcd.putstr("System OFF")

    last_state = current
  
    # SYSTEM ACTIVE
    if system_on:
        dist = get_distance()
        lcd.move_to(0, 1)
        lcd.putstr("Dist: {:>3} cm   ".format(dist))

    time.sleep_ms(100)
