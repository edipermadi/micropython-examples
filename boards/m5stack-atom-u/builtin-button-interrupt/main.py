import time
from machine import Pin

previous = True  # pulled up button, True when released, False when pressed
value = True


# The function will be called when the state of the button changed. A button object will be passed as argument
def button_irq_handler(pin):
    global value
    value = pin.value()


# builtin button connected at G39, externally pulled up
button = Pin(39, Pin.IN)
button.irq(button_irq_handler)

while True:
    if previous != value:
        previous = value
        if not value:
            print('pressed')
        else:
            print('released')

    time.sleep(0.1)
