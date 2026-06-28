from machine import Pin, PWM, Timer
import time

bpm = 80

ms_pb = (1000*60)//bpm
step = ms_pb // 10

def drum1():
    sound = PWM(13, freq=50, duty=500)
    time.sleep_ms(step)
    sound.deinit()

def drum2():
    sound = PWM(13, freq=25, duty=500)
    time.sleep_ms(step)
    sound.deinit()

def pause():
    time.sleep_ms(step)

def drums(t):
    drum1()
    drum2()
    pause()
    
    drum1()
    drum2()
    pause()
    
    drum1()
    drum2()
    drum2()
    pause()

def bass_note1():
    sound = PWM(12, freq=100, duty=200)
    time.sleep_ms(step*4)
    sound.deinit()

def bass_note2():
    sound = PWM(12, freq=150, duty=200)
    time.sleep_ms(step*4)
    sound.deinit()

def bass_note3():
    sound = PWM(12, freq=200, duty=200)
    time.sleep_ms(step*4)
    sound.deinit()

def bass(t):
    bass_note1()
    bass_note2()
    bass_note3()
    bass_note3()
    bass_note2()
    
    bass_note2()
    bass_note1()
    bass_note1()
    bass_note2()
    bass_note3()

print("Done")


timer0 = Timer(0)
timer1 = Timer(1)

print("Done2")

timer0.init(mode=Timer.PERIODIC, period=ms_pb, callback=drums)
print("Done3")
timer1.init(mode=Timer.PERIODIC, period=(ms_pb * 2), callback=bass)
print("Done4")

while True:
    pass

    