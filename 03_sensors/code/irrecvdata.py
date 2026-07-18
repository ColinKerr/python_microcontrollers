from machine import Pin, Timer
import time


"""
Class to read signals from the IR Remote

gpioNum - The number of the GPIO pin the IR Receiver is connected to
commandHandler - The callback function that will be called after a command has been
  decoded from the IR Remote.  
  The Callback function must take an integer in as a parameter, this integer is the 
  hex code for the button pressed.
"""
class irGetCMD(object):
    def __init__(self, gpioNum, commandHandler):
        self.irRecv = Pin(gpioNum, Pin.IN, Pin.PULL_UP)
        self.irRecv.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self.__logHandler)
        self.logList = []
        self.start = 0
        self.cmdHandler = commandHandler
        self.timer = Timer(0)

    def __logHandler(self, source):
        thisComeInTime = time.ticks_us()
        if self.start == 0:
            self.start = thisComeInTime
            self.timer.deinit()
            self.timer.init(mode=Timer.ONE_SHOT, period=120, callback=self.readCommand)
            return
        self.logList.append(time.ticks_diff(thisComeInTime, self.start))
        self.start = thisComeInTime
                        
    def readCommand(self, t):
        if len(self.logList) < 67:
            print("Error reading command")
            self.reset()
        else:
            bufferedBits = []
            for i in range(3, 66, 2):
                if self.logList[i] > 800:
                    bufferedBits.append(1)
                else:
                    bufferedBits.append(0)
            
            irValue=0x00000000
            for b in bufferedBits:
                irValue = irValue<<1
                irValue += b
            
            self.reset()
            self.cmdHandler(irValue)
    
    def reset(self):
        self.logList = []
        self.index = 0
        self.start = 0
       
