# Ultrasonic Ranging (with the hcsr04 module)

Redo [Ultrasonic Ranging](./03_04_ultrasonic_ranging.md) using a pre-built `hcsr04` driver module instead of hand-rolling the trigger/echo timing — much shorter code, same result.

## New Concepts
- Using a driver module to replace manual low-level timing code

---

## Component List & Circuit

*Identical to [Ultrasonic Ranging](./03_04_ultrasonic_ranging.md)*.

---

## Code

**File:** [`03_sensors/code/Ultrasonic_Ranging_2.py`](./code/Ultrasonic_Ranging_2.py)
**Module:** [`03_sensors/code/hcsr04.py`](./code/hcsr04.py)

```python
from hcsr04 import SR04
import time

SR=SR04(13,14)

time.sleep_ms(2000)
try:
    while True:
        print('Distance: ',SR.distance(),'cm')
        time.sleep_ms(500)
except:
    pass
```

---

## How to Run

### Online
1. Open Thonny → `03_sensors/code/`.
2. Right-click `hcsr04.py` → **Upload to /** — wait for it to finish uploading to the ESP32-S3.
3. Double-click `Ultrasonic_Ranging_2.py`.
4. Click **Run current script** — same distance readings as before, with far less code.

---

## Code Explanation

### Create the sensor object

```python
SR=SR04(13,14)
```
`SR04(13,14)` does everything [Ultrasonic Ranging](./03_04_ultrasonic_ranging.md)'s `getSonar()` function did manually — sets up the Trig/Echo pins — but hides it behind one constructor call.

### Read the distance

```python
print('Distance: ',SR.distance(),'cm')
```
`SR.distance()` replaces the entire trigger-pulse-and-timing dance with a single method call, returning the distance in cm as a `float`.

---

## Key Concepts

- **Driver modules**: wrapping repetitive low-level logic (like manual pulse timing) in a reusable class makes application code dramatically shorter and harder to get wrong
- **Uploading dependencies**: any module a script imports (here, `hcsr04.py`) must be uploaded to the device alongside it — the same pattern seen in [Flowing Light with PWM](../02_input_and_output/06_flowing_light_pwm.md)'s `pwm.py`

See [Class hcsr04](../reference/Class_hcsr04.md) for the full API reference, including `distanceCM()` and `distanceMM()`.

## Further Exploration

- Try `SR.distanceMM()` for millimeter precision instead of `distance()`'s centimeters.
- Compare this code's readings against [Ultrasonic Ranging](./03_04_ultrasonic_ranging.md)'s manual version — they should match closely.

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) Project 21.2
