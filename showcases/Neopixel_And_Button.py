from machine import Pin
import neopixel
import time
pin = Pin(48, Pin.OUT)
np = neopixel.NeoPixel(pin, 8)
button = Pin(13, Pin.IN,Pin.PULL_UP)
color_val = 0

#brightness :0-255
brightness=10                                
colors=[[brightness,0,0],					 	          #red
        [brightness, int(brightness / 8), 0],	#orange
        [brightness, int(brightness / 2), 0],	#yellow
        [0,brightness,0],                    	#green
        [0,0,brightness],                    	#blue
        [int(brightness / 2), 0, brightness],	#purple
        [brightness, 0, brightness],			    #pink
        [brightness,brightness,brightness],  	#white
        [0,0,0]]                             	#close

for i in range(0,8): # Turns the LED off at the beginning of the program.
    np[i]=colors[-1]
    np.write()

while True:           
    if not button.value(): # Whenever the button is pressed, the Neopixel will do a monochrome color wheel spin. It can also be held.
        for i in range(0,8):
            np[i]=colors[color_val]
            np.write()
            time.sleep_ms(50)

        if color_val < (len(colors) - 1): # Changes LED's color, if it's greater than the length of the list it'll reset to 0 so that it loops around. Also allows you to add more colors to the list without having to change anything else.
            color_val += 1
        else:
            color_val = 0
