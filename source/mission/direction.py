from Adafruit_MotorHAT import *
import RPi.GPIO as GPIO

from control import *


class Direction():

	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		GPIO.setup(4, GPIO.IN)
		GPIO.setup(17, GPIO.IN)
		GPIO.setup(27, GPIO.IN)
		GPIO.setup(22, GPIO.IN)
		GPIO.setup(18, GPIO.IN)
		GPIO.setup(23, GPIO.IN)
		GPIO.setup(24, GPIO.IN)

	def sensorRead(self):
		#returns sensor read data as an array
		#return [GPIO.input(17), GPIO.input(18), GPIO.input(27), GPIO.input(22), GPIO.input(23), GPIO.input(24)]

		global CFC
		#print CFC
		CFC.update(Direction.sensorRead)

		#return [GPIO.input(4), GPIO.input(17), GPIO.input(18), GPIO.input(27), GPIO.input(22), GPIO.input(23)]
		return [GPIO.input(17), GPIO.input(18), GPIO.input(23), GPIO.input(24)]
		#return [GPIO.input(17), GPIO.input(18), GPIO.input(23]

	def calcWeights(self, sensorData, c=16, baseSpeed = 48, clr = 'black'):
		global CFC
		CFC.update(Direction.calcWeights)
		
		#weights = [-8, -2, 0, 0, 2, 8]
		weights = [-8, -4, 4, 8]
		#weights = [-6, 0, 6]

		numActive = 0
		for i in sensorData:
			if i > 0:
				numActive+=1

		#if numActive <= 0:
			#return [0, 0, Adafruit_MotorHAT.RELEASE, Adafruit_MotorHAT.RELEASE]
		
		if clr not in [ 'black', 'white', '']:
			#print clr
			c = 0		

		dot = 0
		for i in xrange(0, len(weights)):
			dot += weights[i] * sensorData[i]

		weight = dot / numActive

		lSpeed = baseSpeed + c*weight
		rSpeed = baseSpeed - c*weight

		if lSpeed < 0: 
			lSpeed = 0
		if rSpeed < 0:
			rSpeed = 0

		return [lSpeed, rSpeed, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD]


	def __eq__(self, other):
		return self.__dict__ == other.__dict__
		
	def __repr__(self):
		return self.__dict__.__str__()
