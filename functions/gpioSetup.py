from variables import led1, led2, led3
import RPi.GPIO as GPIO

class gpioSetup:
    def __init__(self):
        #Set gpio numbering mode
        GPIO.setmode(GPIO.BOARD)
        #Disable GPIO warnings
        GPIO.setwarnings(False)
        #Set led1, led2 and led3 to outputs
        GPIO.setup(led1, GPIO.OUT)
        GPIO.setup(led2, GPIO.OUT)
        GPIO.setup(led3, GPIO.OUT)
        GPIO.setup(shutdownSwitch, GPIO.OUT)
