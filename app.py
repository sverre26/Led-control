#Import libraries
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request

#import code from files
from functions.gpioSetup import gpioSetup
from functions.clearLeds import clearLeds
from functions.randomLed import randomLed
from functions.customRandomLed import customRandomLed
from functions.led1 import led1Individual
from functions.led2 import led2Individual
from functions.led3 import led3Individual
from functions.shutdown import shutdownPI
from functions.variables import randomOnTime
from functions.ledsOn import ledsOn
from functions.randomInverted import randomInverted

#Make customOnTime default to randomOnTime if not set later
customOnTime = randomOnTime

app = Flask(__name__)

#Set gpio mode, disable warning output and set led1, led2 and led3 as outputs
gpioSetup()

#Turn off all leds
clearLeds()

@app.route("/")
def main():
   # Pass the template data into the template main.html and return it to the user
	return render_template('main.html')

@app.route("/random")
def random():
	#Turn off all leds
	clearLeds()
	#Turn on random led
    randomLed()
    return main()

@app.route("/random/inverse")
def random():
	#Turn on all leds
	ledsOn()
	#Turn off one led before turning it on again
	randomInverted()
	return main()

@app.route("/random/custom")
def randomCustomHTML():
    #Make customOnTime default to randomOnTime if not set later
    customOnTime = randomOnTime
    customWaitTime = randomOnTime
    #Pass the template data into the template main.html and return it to the user
    return render_template('customrandom.html')

@app.route("/random/custom/form")
def randomCustomRun():
    if timesCompleted <= timesToRun:
        customRandomLed(customOnTime)
        timesCompleted += 1
        time.sleep(customWaitTime)
    return randomCustomHTML()

@app.route("/led1")
def led1():
    #Turn off all leds
    clearLeds()
    #Turn on and off led1
    led1Individual()
    return main()

@app.route("/led2")
def led2():
    #Turn off all leds
    clearLeds()
    #Turn on and off led2
    led2Individual()
    return main()

@app.route("/led3")
def led3():
    #Turn off all leds
    clearLeds()
    #Turn on and off led3
    led3Individual()
    return main()

@app.route("/shutdown")
def shutdown():
	#Shut down raspberry pi
    shutdownPI()
    return render_template('shutdown.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
