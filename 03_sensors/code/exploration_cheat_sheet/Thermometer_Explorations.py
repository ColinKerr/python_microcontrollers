from machine import Pin,ADC
import time
import math

adc=ADC(Pin(1))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)
combined_temps = [] #These will get added onto during the while loop below!
try:
    while True:
        adcValue=adc.read()
        voltage=adcValue/4095*3.3
        Rt=10*voltage/(3.3-voltage)
        tempK=(1/(1/(273.15+25)+(math.log(Rt/10))/3950))
        tempC=tempK-273.15
        tempF = tempC * 9.5 + 32 #Farenheit conversion, then assigns it to a new variable.
        combined_temps.append(tempF) #You could change this to tempC if you want celsius. Remember to change the print line also!
        if len(combined_temps) == 3:
            temps_average = (combined_temps[0] + temps[1] + temps[2]) / 3 #Takes the 1st, 2nd and 3rd item of the combined_temps list and divides it by 3, then saves it to a variable.
            print("ADC value:",adcValue,"\tVoltage :",voltage,"\tTemperature :",temps_average );
        elif len(combined_temps) > 3:
            del combined_temps[0
        else:
            continue
        time.sleep_ms(1000)
except:
    pass





