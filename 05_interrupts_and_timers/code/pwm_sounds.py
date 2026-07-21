from machine import Pin, PWM
import time

# Note frequencies
g3 = 196
a3 = 220
b3 = 247

c4 = 262
e4 = 330
d4 = 294

rest = 0

twinkle_notes = [g3, rest, g3, rest, rest, d4, rest, d4, rest, rest, e4, rest, e4, rest, rest, d4, d4, rest, rest, rest, rest,
                 c4, rest, c4, rest, rest, b3, rest, b3, rest, rest, a3, rest, a3, rest, rest, g3, g3, rest, rest, rest, rest,
                 d4, rest, d4, rest, rest, c4, rest, c4, rest, rest, b3, rest, b3, rest, rest, a3, a3, rest, rest, rest, rest,
                 d4, rest, d4, rest, rest, c4, rest, c4, rest, rest, b3, rest, b3, rest, rest, a3, a3, rest, rest, rest, rest,
                 g3, rest, g3, rest, rest, d4, rest, d4, rest, rest, e4, rest, e4, rest, rest, d4, d4, rest, rest, rest, rest,
                 c4, rest, c4, rest, rest, b3, rest, b3, rest, rest, a3, rest, a3, rest, rest, g3, g3, rest, rest, rest, rest]

pin = Pin(11, Pin.OUT)
pwm = PWM(pin, freq = b3, duty = 0)

try:
    for note in twinkle_notes:
        if note > 0:
            pwm.freq(note)
            pwm.duty(512)
        else:
            pwm.duty(0)
        time.sleep_ms(120)
finally:
    pwm.deinit()