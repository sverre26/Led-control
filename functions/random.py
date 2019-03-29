import random as random1
from variables import led1 led2 led3 randomOnTime

class randomLed:
    def __init__(self):
        #Generate random number between 1 and 3
        randomnumber = random1.randint(1,3)
        #Run this code for all pins
        for pin in pins:
            #set pin to low
            GPIO.output(pin, GPIO.LOW)
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
