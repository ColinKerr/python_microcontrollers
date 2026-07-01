from hcsr04 import SR04
import time

SR=SR04(13,14)

time.sleep_ms(2000)

distances = [] #Distance numbers will be added here from the loop, 

try:
    while True:
        if len(distances) == 3:
            avg_distance = (distances[0] + distances[1] + distances[2]) // 3 #Averages the distances
            print('Distance: ',avg_distance,'MM')
            time.sleep_ms(450)
        elif len(distances) > 3:
            del distances[0]
            continue
        distances.append(SR.distanceMM()) #Uses Milimeters instead of Centimeters and appends to list
        time.sleep_ms(50)
except:
    pass

