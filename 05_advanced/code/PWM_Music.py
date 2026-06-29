from machine import Pin, PWM, Timer
import time
from notes import *

bpm = 80

ms_pb = (1000*60)//bpm
step = ms_pb // 10


twinkle_notes = [G, G, P, D, D, P, E, E, DL, PL,
                 C, C, P, B, B, P, A, A, GL, PL,
                 D, D, P, C, C, P, B, B, AL, PL,
                 G, G, P, D, D, P, E, E, DL, PL,
                 C, C, P, B, B, P, A, A, GL]
twinkle = parse_notes(twinkle_notes, step)

print("Done")
timer0 = Timer(0)



play_sequence(twinkle, timer0, 13)

while True:
    pass

    