from machine import Pin, PWM, Timer
import time

class Music:
    def __init__(self):
        self.bpm = 80
        self.ms_pb = (1000*60)//self.bpm
        self.step = self.ms_pb // 10
        self.timer0 = Timer(0)
        self.timer1 = Timer(1)

    def drum1(self):
        sound = PWM(13, freq=50, duty=500)
        time.sleep_ms(self.step)
        sound.deinit()

    def drum2(self):
        sound = PWM(13, freq=25, duty=500)
        time.sleep_ms(self.step)
        sound.deinit()

    def pause(self):
        time.sleep_ms(self.step)

    def drums(self, t):
        self.drum1()
        self.drum2()
        self.pause()
        
        self.drum1()
        self.drum2()
        self.pause()
        
        self.drum1()
        self.drum2()
        self.drum2()
        self.pause()

    def base_note1(self):
        sound = PWM(12, freq=100, duty=200)
        time.sleep_ms(self.step*4)
        sound.deinit()

    def base_note2(self):
        sound = PWM(12, freq=150, duty=200)
        time.sleep_ms(self.step*4)
        sound.deinit()

    def base_note3(self):
        sound = PWM(12, freq=200, duty=200)
        time.sleep_ms(self.step*4)
        sound.deinit()

    def bass(self, t):
        self.base_note1()
        self.base_note2()
        self.base_note3()
        self.base_note3()
        self.base_note2()
        
        self.base_note2()
        self.base_note1()
        self.base_note1()
        self.base_note2()
        self.base_note3()
    
    def start(self):
        self.timer0.init(mode=Timer.PERIODIC, period=self.ms_pb, callback=self.drums)
        self.timer1.init(mode=Timer.PERIODIC, period=(self.ms_pb * 2), callback=self.bass)

music = Music()
music.start()

while True:
    pass

    
