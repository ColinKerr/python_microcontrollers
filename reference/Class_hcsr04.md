# Class hcsr04

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) — Chapter 21, Ultrasonic Ranging

Before each use of the object **SR04**, add the statement `from hcsr04 import SR04` to the top of the Python file.

- **`SR04()`**: Object for the ultrasonic module. By default, the trig pin is Pin(13) and the echo pin is Pin(14).
- **`distanceCM()`**: Obtains the distance from the ultrasonic sensor to the measured object as an `int`, in cm.
- **`distanceMM()`**: Obtains the distance from the ultrasonic sensor to the measured object as an `int`, in mm.
- **`distance()`**: Obtains the distance from the ultrasonic sensor to the measured object as a `float`, in cm.
