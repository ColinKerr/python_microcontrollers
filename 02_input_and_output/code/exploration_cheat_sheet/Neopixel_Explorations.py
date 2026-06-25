from machine import Pin
import neopixel
import time
pin = Pin(48, Pin.OUT)
np = neopixel.NeoPixel(pin, 8)

#brightness :0-255
brightness=15 #Not sure what happens if you go too bright                                
colors=[[brightness,0,0],                    #red
        [0,brightness,0],                    #green
        [0,0,brightness],                    #blue
        [150, 5, brightness],                #Run this and find out!
        [brightness,brightness,brightness],  #white
        [0,0,0]]                             #close
    
while True:
    for i in range(0,5):
        for j in range(0,8):
            np[j]=colors[i]
            np.write()
            time.sleep_ms(50)
        time.sleep_ms(500)
    time.sleep_ms(500)
    
    

