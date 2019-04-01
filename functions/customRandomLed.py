import random
import time
import RPi.GPIO as GPIO
from variables import led1, led2, led3, randomOnTime
class randomLed:
    def __init__(self):
        #Generate random number between 1 and 3
        randomnumber = random.randint(1,3)
        #Run code only for the pin selected by the random number
        if randomnumber == 1:
            GPIO.output(led1, GPIO.HIGH)
            time.sleep(randomOnTime)
            GPIO.output(led1, GPIO.LOW)
        elif randomnumber == 2:
            GPIO.output(led2, GPIO.HIGH)
            time.sleep(randomOnTime)
            GPIO.output(led2, GPIO.LOW)
        elif randomnumber == 3:
            GPIO.output(led3, GPIO.HIGH)
            time.sleep(randomOnTime)
            GPIO.output(led3, GPIO.LOW)
