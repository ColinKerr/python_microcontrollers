from machine import Pin, PWM
import time


class ultrasonic:
    
    def __init__(self, pinNum):
        self.echoPin = Pin(pinNum, Pin.IN, 0)
        self.startEcho = 0
        self.endEcho = 0
        self.distance = 0
        self.lastMeasure = 0
        self.soundVelocity=340
        self.echoPin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self.measure)

    def measure(self, pin):
        if pin.value():
            self.startEcho = time.ticks_us()
        else:
            self.endEcho = time.ticks_us()
            self.distance = self.calculateCM(self.startEcho, self.endEcho)
            self.lastMeasure = self.endEcho
            print("Distance: ", self.distance, "CM")

    def calculateCM(self, start, stop):
        ticks=time.ticks_diff(stop,start)
        return int(ticks*self.soundVelocity//2//10000)


trigPulse = PWM(Pin(13, Pin.OUT), freq=10, duty=1)
us = ultrasonic(14)

time.sleep_ms(2000)
while True:
    pass
    
    
    
    
    
    
    
    
    
    
    
    
    