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
	server = PiServer()
	server.keyExchange()

	target = 'blue'

	atexit.register(motors.turnOff)
	
	print 'starting this shit'
	while(True):
		#Make calls to other files

		sensorData = direction.sensorRead()
		colorReading = colorSensor.readColor()
		color = colorSensor.distance(colorReading)
		try:
			inp = server.operation()
			if inp != None:
				target = inp
		except Exception, e:
			raise e

		print target, color, colorReading, sensorData

		if color == target:
			print 'found target, exiting'
			exit()
		else:	

			try:
				[lSpeed, rSpeed, lDir, rDir] = direction.calcWeights(sensorData)
				motors.drive(lSpeed, rSpeed, lDir, rDir)
			except ZeroDivisionError as e:
				#print e
				2+2
				#motors.turnOff()


			
if __name__ == '__main__':
	mission()
