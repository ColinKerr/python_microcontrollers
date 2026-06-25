from machine import Pin,PWM,ADC
import time

pwm =PWM(Pin(14,Pin.OUT),1000)
adc=ADC(Pin(1))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

def remap(value,oldMin,oldMax,newMin,newMax):
    return int((value)*(newMax-newMin)/(oldMax-oldMin))

try:
    while True:
        adcValue=adc.read()
        pwmValue=remap(adcValue,0,4095,0,512) #See what happens when you change the numbers!
        pwm.duty(pwmValue)
        print(adcValue,pwmValue)
        time.sleep_ms(120) #You can make it lag behind or go super smooth by changing the wait time!
except:
    adc.deinit()
    pwm.deinit()





