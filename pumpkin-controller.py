from microbit import *
from microbit import sleep
import radio
# The radio won't work unless it's switched on.
radio.on()
while True:
    gesture = accelerometer.current_gesture()
    if gesture == "face up":
        radio.send("face up")
    elif gesture == "shake":
        radio.send("shake")
    elif gesture == "left":
        radio.send("left")
    elif gesture == "right":
        radio.send("right")
    elif gesture == "up":
        radio.send("up")
    elif gesture == "down":
        radio.send("down")
    sleep(50)