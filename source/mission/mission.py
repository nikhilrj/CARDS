#Mission.py handles all overhead mission operation
from motors import *
from color import *
from server import *
from direction import *

import os, atexit, time, atexit

def mission():
	motors = MotorDriver()
	colorSensor = ColorSensor()
	direction = Direction()

	atexit.register(motors.turnOff)

	while(True):
		#Make calls to other files
		sensorData = direction.sensorRead()
		colorReading = colorSensor.readColor()
		color = colorSensor.distance(colorReading)

		print color, colorReading, sensorData

		try:
			[lSpeed, rSpeed, lDir, rDir] = direction.calcWeights(sensorData)
			motors.drive(lSpeed, rSpeed, lDir, rDir)
		except ZeroDivisionError as e:
			print e
			motors.turnOff()
			
if __name__ == '__main__':
	mission()
