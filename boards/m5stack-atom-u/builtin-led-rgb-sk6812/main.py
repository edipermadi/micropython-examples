import time
import random
from machine import Pin
from neopixel import NeoPixel

pin = Pin(27, Pin.OUT)
np = NeoPixel(pin, 1)  # 1 LED only

# color choices
choices = [
    [0, 0, 51],
    [0, 51, 0],
    [0, 51, 51],
    [51, 0, 0],
    [51, 0, 51],
    [51, 51, 0],
    [51, 51, 51],
]


def increase(value, new_value):
    return value + 1 if value < new_value else value


def decrease(value):
    return value - 1 if value > 0 else value


def update(red, green, blue):
    np[0] = (red * 5, green * 5, blue * 5, 0)
    np.write()


# pick color, brighten up then fade away
while True:
    red, green, blue = 0, 0, 0
    (new_red, new_green, new_blue) = random.choice(choices)

    time.sleep(0.2)
    for i in range(51):
        red = increase(red, new_red)
        green = increase(green, new_green)
        blue = increase(blue, new_blue)
        update(red, green, blue)
        time.sleep(0.05)

    time.sleep(0.2)
    for i in range(51):
        red = decrease(red)
        green = decrease(green)
        blue = decrease(blue)
        update(red, green, blue)
        time.sleep(0.05)
