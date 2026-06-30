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
      mode = zVal.value()
      joystick_x = xVal.read()
      joystick_y = yVal.read()
      if mode == 0:
          print("X,Y,Z:",joystick_x,",",joystick_y,"Mode: Simple")
      else:
          print("X,Y,Z:",xVal.read(),",",yVal.read(),"Mode: Default / Accurate")
      time.sleep(1)
except:
    xVal.deinit()
    yVal.deinit()

  
  
  
  
  
