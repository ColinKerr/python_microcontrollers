from machine import ADC,Pin
import time

xVal=ADC(Pin(14))
yVal=ADC(Pin(13))
zVal=Pin(12,Pin.IN,Pin.PULL_UP)

xVal.atten(ADC.ATTN_11DB)
yVal.atten(ADC.ATTN_11DB)
xVal.width(ADC.WIDTH_12BIT)
yVal.width(ADC.WIDTH_12BIT)


try:
    while True:
      joystick_x = int((xVal.read() - 0) * (100 - -100) / (4095 - 0) + -100) #This is very similar to a function used in Soft Light, but slightly different. For simplicity this code isn't made into a function.
      joystick_y = int((yVal.read() - 0) * (100 - -100) / (4095 - 0) + -100)
      
      if zVal.value() == 0: #Conditional that checks if the joystick is pressed down
          print("X,Y,Z:",joystick_x,",",joystick_y,"Mode: Simplified")
      else:
          print("X,Y,Z:",xVal.read(),",",yVal.read(),"Mode: Accurate")
      time.sleep(1)
except:
    xVal.deinit()
    yVal.deinit()

  
  
  
  
  
