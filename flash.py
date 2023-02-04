from machine import Pin
from time import sleep_ms

pin = Pin("LED", Pin.OUT)

while True:
    pin.toggle()
    sleep_ms(1000)
    