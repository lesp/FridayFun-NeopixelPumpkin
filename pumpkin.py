import radio
import random
from microbit import *
from microbit import sleep
import neopixel

np = neopixel.NeoPixel(pin0, 7)

# The radio won't work unless it's switched on.
radio.on()

# Event loop.
while True:
    incoming = radio.receive()
    #sleep(100)
    #incoming = str(incoming)
    #sensor = sensor.split(sep=',')
    if incoming == "face up":
        print("face up")
        for i in range(7):
            np[i] = (255,0,0)
            np.show()
        sleep(50)     
    elif incoming == "shake":
        print("shake")
        for i in range(7):
            np[i] = (255,69,0)
            np.show()
        sleep(50)  
    elif incoming == "left":
        print("left")
        for i in range(7):
            np[i] = (0,255,0)
            np.show()
        sleep(50)  
    elif incoming == "right":
        print("right")
        for i in range(7):
            np[i] = (255,0,255)
            np.show()
        sleep(50)  
    elif incoming == "up":
        print("up")
        for i in range(7):
            np[i] = (0,191,255)
            np.show()
        sleep(50)  
    elif incoming == "down":
        print("down")
        for i in range(7):
            np[i] = (124,252,0)
            np.show()
        sleep(50) 
    else:
        for i in range(7):
            np[i] = (0,0,0)
            np.show()
        sleep(50)  

    #if incoming == 'flash':
    #    print("Hello")