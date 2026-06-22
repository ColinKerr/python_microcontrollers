# Rainbow Light

Make all 8 LEDs on the RGB LED Module display a smooth, evenly-spaced rainbow that continuously shifts — combining the [LED Pixel](./08_led_pixel.md) module with the color-wheel technique from [Gradient Color Light](./07_gradient_color_light.md).


## Component List

*Same module, board, and circuit as [LED Pixel](./08_led_pixel.md).*

---

## Circuit

*Same circuit as [LED Pixel](./08_led_pixel.md) — see that page for the schematic and wiring diagrams.*

---

## Code

**File:** [`02_input_and_output/code/Rainbow_light.py`](./code/Rainbow_light.py)

```python
from machine import Pin
import neopixel
import time
pin = Pin(48, Pin.OUT)
np = neopixel.NeoPixel(pin, 8)

brightness=0.1         #brightness: 0-1.0
red=0                  #red
green=0                #green
blue=0                 #blue

def wheel(pos):
    global red,green,blue
    WheelPos=pos%255
    if WheelPos<85:
        red=(255-WheelPos*3)
        green=(WheelPos*3)
        blue=0
    elif WheelPos>=85 and WheelPos<170:
        WheelPos -= 85;
        red=0
        green=(255-WheelPos*3)
        blue=(WheelPos*3)
    else :
        WheelPos -= 170;
        red=(WheelPos*3)
        green=0
        blue=(255-WheelPos*3)
        
while True:
    for i in range(0,255):
        for j in range(0,8):
            wheel(i+j*255//8)
            np[j]=(int(red*brightness),int(green*brightness),int(blue*brightness))
            np.write()
        time.sleep_ms(5)
```

---

## How to Run

### Online
1. Open Thonny → `02_input_and_output/code/`.
2. Double-click `Rainbow_light.py`.
3. Click **Run current script** — the 8 LEDs display a rainbow that shifts smoothly along the strip.

---

## Code Explanation

### The color wheel function

```python
def wheel(pos):
    global red,green,blue
    WheelPos=pos%255
    if WheelPos<85:
        red=(255-WheelPos*3)
        green=(WheelPos*3)
        blue=0
    elif WheelPos>=85 and WheelPos<170:
        WheelPos -= 85
        red=0
        green=(255-WheelPos*3)
        blue=(WheelPos*3)
    else:
        WheelPos -= 170
        red=(WheelPos*3)
        green=0
        blue=(255-WheelPos*3)
```
Same idea as [Gradient Color Light](./07_gradient_color_light.md)'s `wheel()`, but using a 0–255 range (since `np[j]` expects 0–255 color bytes, not 0–1023 PWM duty values) and setting `red`/`green`/`blue` globals instead of writing to PWM pins directly.

### Spread the wheel across all 8 LEDs

```python
for i in range(0,255):
    for j in range(0,8):
        wheel(i+j*255//8)
        np[j]=(int(red*brightness),int(green*brightness),int(blue*brightness))
        np.write()
    time.sleep_ms(5)
```
For LED `j`, the wheel position is offset by `j*255//8` — so each of the 8 LEDs sits at an evenly-spaced point around the wheel (1/8th of the way apart) instead of all showing the same color. As `i` increases, every LED's position shifts together, sliding the rainbow along the strip. `brightness` (0.0–1.0) scales the final RGB values down before they're written.

---

## Key Concepts

- **Per-LED phase offset**: adding `j*255//8` to the wheel position spreads one color cycle evenly across 8 LEDs instead of showing one color at a time
- **Brightness scaling**: multiplying each color channel by a 0–1.0 `brightness` value dims the whole strip without changing the color math

See [Class neopixel](../reference/Class_neopixel.md) for the full API reference.

## Further Exploration

- Change `brightness` to 1.0 for full intensity, or near 0 for a dim glow.
- Change the divisor in `j*255//8` to make the rainbow repeat more than once across the strip.

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) Project 6.2
