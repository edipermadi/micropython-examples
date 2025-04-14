from wavplayer import WavPlayer
from machine import Pin
from time import sleep

wp = WavPlayer(id=0, sck_pin=Pin(19), ws_pin=Pin(33), sd_pin=Pin(22), ibuf=65536, root="/")

playing = False

def handle_button(pin):
    global playing
    playing = not playing

btn = Pin(39, Pin.IN)
btn.irq(trigger=Pin.IRQ_RISING, handler=handle_button)

while True:
    sleep(2)
    if playing:
        wp.play("metronome.wav", loop=False)
