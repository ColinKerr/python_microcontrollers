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
        pwmValue=remap(adcValue,0,4095,0,1023)
        if adcValue < 2850: # If light level is at a regular amount the light will be at max brightness.
            pwm.duty(pwmValue)
        elif 2850 <= adcValue < 3600: # If it starts decreasing the light will dim as well.
            pwm.duty(512)
        else: # This is the threshold for how dark it can get before the LED turns off, if you were just doing the second exploration this would be brighter / on.
            pwm.duty(0)
            time.sleep_ms(10)
            pwm.duty(512)
        print(adcValue,pwmValue)
except:
    adc.deinit()
    pwm.deinit()
