#Import libraries
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request

#import code from files
from functions.gpio-setup import gpioSetup
from functions.clearLeds import clearLeds
from functions.random import randomLed
from functions.led1 import led1Individual
from functions.led2 import led2Individual
from functions.led3 import led3Individual
from functions.shutdown import shutdown

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
    randomNumber()
    return main()

@app.route("/led1")
def led1():
	# #Run this code for all pins
    # #set pin to low
	# for pin in pins:
	# 	GPIO.output(pin, GPIO.LOW)
	# #Turn on led 1
	# GPIO.output(37, GPIO.HIGH)
	# #Wait
	# time.sleep(onTime)
	# #Turn led 1 off
	# GPIO.output(37, GPIO.LOW)
	return main()

@app.route("/led2")
def led2():
	# #Run this code for all pins
	# for pin in pins:
	# 	#set pin to low
	# 	GPIO.output(pin, GPIO.LOW)
	# #Turn on led 2
	# GPIO.output(38, GPIO.HIGH)
	# #Wait
	# time.sleep(onTime)
	# #Turn led 2 off
	# GPIO.output(38, GPIO.LOW)
	return main()

@app.route("/led3")
def led3():
	# #Run this code for all pins
	# for pin in pins:
	# 	#set pin to low
	# 	GPIO.output(pin, GPIO.LOW)
	# #Turn on led 3
	# GPIO.output(40, GPIO.HIGH)
	# #Wait
	# time.sleep(onTime)
	# #Turn led 3 off
	# GPIO.output(40, GPIO.LOW)
	return main()

@app.route("/shutdown")
def shutdown():
	#Shut down raspberry pi

	return

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
