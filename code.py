import time
import board
from analogio import AnalogIn
#from picoed import display, Image
from picoed import *
from digitalio import DigitalInOut, Direction

# Level water sensor
waterlevel = AnalogIn(board.A1)
# Humidity sensor
humidity = AnalogIn(board.A2)
# Motor
motor = DigitalInOut(board.A3)
motor.direction = Direction.OUTPUT
# Constants
secondsmotorworks = 1

def get_voltage(pin):
    return (pin.value * 3.3) / 65536

while True:
    #print((get_voltage(humidity),))
    if button_a.is_pressed():
        secondsmotorworks+=1
        if secondsmotorworks > 10:
            secondsmotorworks = 1
        display.show(secondsmotorworks)
        time.sleep(1)
        continue
    if button_b.is_pressed():
        if (get_voltage(waterlevel)) > 1:
            display.show(Image.CRY)
            motor.value = True
            time.sleep(secondsmotorworks)
            motor.value = False
            continue
    if get_voltage(humidity) > 1:
        display.show(Image.HAPPY)
    else:
        if (get_voltage(waterlevel)) > 1:
            display.show(Image.CRY)
            motor.value = True
            time.sleep(secondsmotorworks)
            motor.value = False
            continue
        else:
            display.show(Image.SAD)
    time.sleep(10)