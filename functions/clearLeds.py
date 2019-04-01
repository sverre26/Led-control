from variables import led1, led2, led3
import RPi.GPIO as GPIO

class clearLeds:
    def __init__(self):
        #Turn pins led1, led2 and led3 to low
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
        GPIO.output(led3, GPIO.LOW)
