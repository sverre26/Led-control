from variables import led2, onTime
import time

class led2Individual:
    def __init__(self):
        #Turn on led 1
        GPIO.output(led2, GPIO.HIGH)
        time.sleep(onTime)
        #Wait
        #Turn led 1 off
        GPIO.output(led2, GPIO.LOW)
