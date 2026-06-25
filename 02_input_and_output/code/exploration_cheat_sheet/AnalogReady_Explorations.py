from machine import ADC,Pin
import time

adc=ADC(Pin(1))
adc.atten(ADC.ATTN_6DB) #Notice a difference in the readings at all?
adc.width(ADC.WIDTH_12BIT)

try:
    while True:
        adcVal=adc.read()
        voltage = adcVal / 4095.0 * 3.3
        print("ADC Val:",adcVal,"\tVoltage:", round(voltage, 2),"V") #The round function makes it so that there's only a max of 2 decimal placements, making the output much cleaner looking! Try removing the round( ,2) or increasing/decreasing the number!
        time.sleep_ms(100)
except:
    adc.deinit()



