# Ultrasonic Ranging with Interrupts

We have previously measured distance using the HC-SR04 ultrasonic sensor using sleep and loops to send the pulse and measure the time it takes for the pulse to bounce back.  This works but means the microcontroller cannot do anything while getting the distance measurement.  There is another way to run the ultrasonic sensor without using up all the microcontrollers CPU time ... interrupts

New Concepts:
- Interrupts
- Callback functions

## Component List

![Components](../images/03_04_components.png)

## Circuit

> The HC-SR04 runs on 5V, not 3.3V — make sure VCC is wired to the 5V rail.

### Wiring Diagram

> Disconnect all power before building the circuit. Reconnect once verified.


![Wiring Diagram](../images/03_04_wiring_diagram.png)

**Connections:**
- HC-SR04 Vcc → 5V
- HC-SR04 Trig → GPIO13
- HC-SR04 Echo → GPIO14
- HC-SR04 Gnd → GND

### Schematic Diagram

![Schematic Diagram](../images/03_04_schematic_diagram.png)

## Code

**File:** [`05_advanced/code/Ultrasonic_Ranging.py`](./code/Ultrasonic_Ranging.py)

```python

```

---

## How to Run

### Online
1. Open Thonny → `03_sensors/code/`.
2. Double-click `Ultrasonic_Ranging.py`.
3. Click **Run current script**. After a 2-second warm-up, the Shell prints the measured distance every 500ms — move an object closer or further away and watch it change.

---

## Code Explanation

### Fire a trigger pulse

```python

```
Holds `Trig` HIGH for about 10 microseconds, telling the HC-SR04 to send an ultrasonic pulse.

### Time the echo

```python
```

Constructs an interrupt that is triggered when `Echo` to goes from LOW to HIGH (the pulse has been sent), and when it goes from HIGH to LOW (the echo was received).  On each trigger it runs the callback function.

```python
```

When called on the rising edge (pin.value() == 1) the start ticks are saved.  When called on the falling eduge (pin.value() == 0) the end ticks are saved and distance is calculated.

## Key Concepts

- **interrupts**: 
- **callback functions**: 


## Further Exploration

- 

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) Project 21.1
