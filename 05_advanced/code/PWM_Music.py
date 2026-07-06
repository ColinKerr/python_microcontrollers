from machine import Pin, PWM, Timer
import time
from MusicPlayer import *

bpm = 120

ms_pb = int((1000*60)//bpm)
note_time = int(ms_pb // 4)



voice_groups = load_voice_groups_from_file("nothing_else_matters.lines")
line_length = len(voice_groups[0][0])
line_time = note_time * line_length

print("Number of voice groups:", len(voice_groups))
print("Time per group:", line_time, "ms")
for voice_group in voice_groups:
    print("Number of voices in group:", len(voice_group))

pins = [Pin(11, Pin.OUT), Pin(12, Pin.OUT), Pin(13, Pin.OUT), Pin(14, Pin.OUT)]

player = MusicPlayer(voice_groups, note_time, pins)
player.start()


while player.playing:
    pass

print("Done playing song")