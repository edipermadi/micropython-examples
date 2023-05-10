import time
from machine import Pin

# builtin button connected at G39, externally pulled up
button = Pin(39, Pin.IN)
previous = True  # pulled up button, True when released, False when pressed
while True:
    value = button.value()
    if previous != value:
        previous = value
        if not value:
            print('pressed')
        else:
            print('released')

    time.sleep(0.1)
