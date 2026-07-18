from machine import Pin, Timer
import dht

DHT = dht.DHT11(Pin(21))

def getTemperature(t):
    DHT.measure()
    print('temperature:',DHT.temperature(),'humidity:',DHT.humidity())

timer = Timer(0)
timer.init(mode=Timer.PERIODIC, period=2000, callback=getTemperature)

    
    

    
    
    
    
    
    
    


