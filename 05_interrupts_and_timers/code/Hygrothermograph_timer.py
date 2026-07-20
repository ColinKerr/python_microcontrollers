from machine import Pin, Timer
import dht

DHT = dht.DHT11(Pin(21))

def getTemperature(t):
    DHT.measure()
    print('temperature:',DHT.temperature(),'humidity:',DHT.humidity())

try:
    timer = Timer(0)
    timer.init(mode=Timer.PERIODIC, period=2000, callback=getTemperature)
    
    while True:
        pass
finally:
    timer.deinit()
    
    

    
    
    
    
    
    
    


