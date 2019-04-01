from variables import led1, onTime
import time
import RPi.GPIO as GPIO

class led1Individual:
    def __init__(self):
        #Turn on led 1
        GPIO.output(led1, GPIO.HIGH)
        time.sleep(onTime)
        #Wait
        #Turn led 1 off
        GPIO.output(led1, GPIO.LOW)
