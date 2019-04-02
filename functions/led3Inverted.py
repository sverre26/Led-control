from variables import led3, offTime
import time
import RPi.GPIO as GPIO

class led3Inverted:
    def __init__(self):
        #Turn on led 1
        GPIO.output(led3, GPIO.LOW)
        time.sleep(onTime)
        #Wait
        #Turn led 1 off
        GPIO.output(led3, GPIO.HIGH)
