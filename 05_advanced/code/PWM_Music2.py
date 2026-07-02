#from machine import Pin, PWM, Timer
import time
from notes2 import *

bpm = 89

ms_pb = (1000*60)//bpm
step = ms_pb // 16


note_line_groups = read_notes_from_file("mario.lines")
voice_groups = parse_note_line_groups(note_line_groups)
line_length = len(voice_groups[0][0])
line_time = ms_pb * line_length

print("Number of voice groups:", len(voice_groups))
print("Time per group:", line_time, "ms")
for voice_group in voice_groups:
    print("Number of voices in group:", len(voice_group))

print("Done")
timer0 = Timer(0)

    
