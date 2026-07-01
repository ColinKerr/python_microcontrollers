from machine import Pin
import time

trigPin=Pin(13,Pin.OUT,0)
echoPin=Pin(14,Pin.IN,0)

soundVelocity=340
distance=0

def getSonar():
    trigPin.value(1)
    time.sleep_us(10)
    trigPin.value(0)
    while not echoPin.value():
        pass
    pingStart=time.ticks_us()
    while echoPin.value():
        pass
    pingStop=time.ticks_us()
    pingTime=time.ticks_diff(pingStop,pingStart)
    distance=pingTime*soundVelocity//2//10000
    if pingTime < 80000: #If Sonar takes too long to ping, it'll return None instead of an int.
        return int(distance)
    else:
        print("Couldn't get distance")
        return

time.sleep_ms(2000)
while True:
    current_distance = getSonar()
    time.sleep_ms(500)
    print('Distance: ',current_distance,'cm' )
    if current_distance <= 5: #If something is too close to the Sonar, the user gets notified.
        print("Sonar is too close!")
    
    
    
    
    
    
    
    
    
    
    
    
