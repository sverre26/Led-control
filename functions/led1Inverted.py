from variables import led1, offTime
import time
import RPi.GPIO as GPIO

class led1Inverted:
    def __init__(self):
        #Turn on led 1
        GPIO.output(led1, GPIO.LOW)
        #Wait
        time.sleep(offTime)
        #Turn led 1 off
        GPIO.output(led1, GPIO.HIGH)
