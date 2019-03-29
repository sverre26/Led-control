#Import libraries
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request

#import code from files
from functions/random.py import randomLed

app = Flask(__name__)

#Set gpio mode and disable warning output
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Define number of seconds the leds will stay on
randomOnTime = 3
onTime = 3

#Define pin numbers

pins = {
   37 : {'name' : 'led1', 'state' : GPIO.LOW},
   38 : {'name' : 'led2', 'state' : GPIO.LOW},
   40 : {'name' : 'led3', 'state' : GPIO.LOW}
   }

#Run this code for all pins
for pin in pins:
   #Set pin as output
   GPIO.setup(pin, GPIO.OUT)
   #set pin to low
   GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   # Pass the template data into the template main.html and return it to the user
	return render_template('main.html')

@app.route("/random")
def random():
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
	return main()

@app.route("/led1")
def led1():
	#Run this code for all pins
	for pin in pins:
		#set pin to low
		GPIO.output(pin, GPIO.LOW)
	#Turn on led 1
	GPIO.output(37, GPIO.HIGH)
	#Wait
	time.sleep(onTime)
	#Turn led 1 off
	GPIO.output(37, GPIO.LOW)
	return main()

@app.route("/led2")
def led2():
	#Run this code for all pins
	for pin in pins:
		#set pin to low
		GPIO.output(pin, GPIO.LOW)
	#Turn on led 2
	GPIO.output(38, GPIO.HIGH)
	#Wait
	time.sleep(onTime)
	#Turn led 2 off
	GPIO.output(38, GPIO.LOW)
	return main()

@app.route("/led3")
def led3():
	#Run this code for all pins
	for pin in pins:
		#set pin to low
		GPIO.output(pin, GPIO.LOW)
	#Turn on led 3
	GPIO.output(40, GPIO.HIGH)
	#Wait
	time.sleep(onTime)
	#Turn led 3 off
	GPIO.output(40, GPIO.LOW)
	return main()

@app.route("/shutdown")
def shutdown():
	#Shut down raspberry pi

	return

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
