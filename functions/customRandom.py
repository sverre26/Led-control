import random
import time
from variables import led1, led2, led3, randomOnTime

class randomLed:
    def __init__(self):
        #Generate random number between 1 and 3
        randomnumber = random.randint(1,3)
        #Run this code for all pins
        if randomnumber == 1:
            GPIO.output(37, GPIO.HIGH)
            time.sleep(randomOnTime)
            GPIO.output(37, GPIO.LOW)
        elif randomnumber == 2:
            GPIO.output(38, GPIO.HIGH)
            time.sleep(randomOnTime)
            GPIO.output(38, GPIO.LOW)
        elif randomnumber == 3:
            GPIO.output(40, GPIO.HIGH)
            time.sleep(randomOnTime)
            GPIO.output(40, GPIO.LOW)
