import RPi.GPIO as GPIO
from subprocess import call
from variables import shutdownSwitch

class shutdownPI:
    def __init__(self):
        print "Shuting down"
        GPIO.output(shutdownSwitch, GPIO.HIGH)
        call("sudo shutdown -h now", shell=True)
