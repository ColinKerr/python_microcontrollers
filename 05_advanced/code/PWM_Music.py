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



#play_sequence(twinkle, timer0, Pin(13, Pin.OUT))

mario_notes = ["E_44" , "E_44", "E_44", "C_44", "E_44", "G_44", "G_44", "C_44", 
               "G_44", "E_44", "A_44", "B_44", "AS44", "A_44", "G_44", "E_44", 
               "G_44", "A_44", "F_44", "G_44", "E_44", "C_44", "D_44", "B_44", 
               "C_44", "G_44", "E_44", "A_44", "B_44", "AS44", "A_44", "G_44", 
               "E_44", "G_44", "A_44", "F_44", "G_44", "E_44", "C_44", "D_44", 
               "B_44", "G_44", "FS44", "F_44", "DS44", "E_44", "GS44", "A_44", 
               "C_44", "A_44", "C_44", "D_44", "G_44", "FS44", "F_44", "DS44", 
               "E_44", 
               #"G_44"+"A_44"+"C_44", "G_44"+"A_44"+"C_44", "G_44"+"A_44"+"C_44",
               "G_44", "FS44", "F_44", "DS44", "E_44", "GS44", "A_44", "C_44",
               "A_44", "C_44", "D_44", "DS44", "D_44", "C_44", "C_44", "G_44", 
               "E_44", "A_44", "B_44", "A_44", "GS44", "AS44", "GS44", "G_44", "F_44",  "G_44"]

mario_notes2 = [E, E, E, C, E, G, G, C,
                 G, E, A, B, AS, A, G, E,
                 G, A, F, G, E, C, D, B,
                 C, G, E, A, B, AS, A, G,
                 E, G, A, F, G, E, C, D,
                 B, G, FS, F, DS, E, GS, A,
                 C, A, C, D, G, FS, F, DS,
                 E, G, FS, F, DS, E, GS, A,
                 C, A, C, D, DS, D, C, C,
                 G, E, A, B, A, GS, AS, GS,
                 G, F, G]

mario = parse_notes(mario_notes2, step)
play_sequence(mario, timer0, Pin(13, Pin.OUT))

while True:
    pass

    