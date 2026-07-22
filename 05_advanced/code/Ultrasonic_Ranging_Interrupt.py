from ultrasonic import Ultrasonic

us = Ultrasonic(14, 13)
lastMeasure = us.lastMeasure

while True:
    if lastMeasure != us.lastMeasure:
        print ("Distance:", us.distance, "CM")
        lastMeasure = us.lastMeasure
