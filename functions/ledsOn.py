from variables import led1, led2, led3
import RPi.GPIO as GPIO

class ledsOn:
    def __init__(self):
        #Turn pins led1, led2 and led3 to high (on)
        GPIO.output(led1, GPIO.HIGH)
        GPIO.output(led2, GPIO.HIGH)
        GPIO.output(led3, GPIO.HIGH)
