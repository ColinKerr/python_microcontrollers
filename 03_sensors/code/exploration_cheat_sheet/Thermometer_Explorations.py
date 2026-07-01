from machine import Pin,ADC
import time
import math

adc=ADC(Pin(1))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)
temps = [] #These will get added onto during the while loop below!
try:
    while True:
        adcValue=adc.read()
        voltage=adcValue/4095*3.3
        Rt=10*voltage/(3.3-voltage)
        tempK=(1/(1/(273.15+25)+(math.log(Rt/10))/3950))
        tempC=tempK-273.15
        tempF = tempC * 9.5 + 32 #Farenheit conversion, then assigns it to a new variable.
        if len(temps) == 3:
            temps_combined = round((temps[0] + temps[1] + temps[2]) / 3, 2)
            print("ADC value:",adcValue,"\tVoltage :",voltage,"\tTemperature :",temps_combined );
        if len(temps) > 3:
            del temps[0]
            continue
        temps.append(tempF) #You could change this to tempC if you want celsius.
        time.sleep_ms(1000)
except:
    pass





