import time
import random
from machine import Pin
from neopixel import NeoPixel

pin = Pin(27, Pin.OUT)
np = NeoPixel(pin, 1)  # 1 LED only

choices = [
    [0, 0, 51],
    [0, 51, 0],
    [0, 51, 51],
    [51, 0, 0],
    [51, 0, 51],
    [51, 51, 0],
]

# pick color, brighten up then fade away
while True:
    red, green, blue = 0, 0, 0
    (new_red, new_green, new_blue) = random.choice(choices)

    for i in range(51):
        if red < new_red:
            red += 1

        if green < new_green:
            green += 1

        if blue > new_blue:
            blue -= 1

        np[0] = (red * 5, green * 5, blue * 5, 0)
        np.write()
        time.sleep(0.05)

    time.sleep(0.2)

    for i in range(51):
        if red > 0:
            red -= 1

        if green > 0:
            green -= 1

        if blue > 0:
            blue -= 1

        np[0] = (red * 5, green * 5, blue * 5, 0)
        np.write()
        time.sleep(0.05)

    time.sleep(0.2)
