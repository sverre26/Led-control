from variables import led2, offTime
import time
import RPi.GPIO as GPIO

class led2Inverted:
    def __init__(self):
        #Turn on led 1
        GPIO.output(led2, GPIO.LOW)
        #Wait
        time.sleep(offTime)
        #Turn led 1 off
        GPIO.output(led2, GPIO.HIGH)
