#Mission.py handles all overhead mission operation
from control import *

from motors import *
from color import *
from server import *
from direction import *
from variable import *

import os, atexit, time, atexit

def buildControlGraph():
	global CFC
	CFC.buildGraph(Direction.sensorRead, [None, MotorDriver.drive, Direction.calcWeights])
	CFC.buildGraph(ColorSensor.readColor, [Direction.sensorRead]) 
	CFC.buildGraph(ColorSensor.distance, [ColorSensor.readColor])
	CFC.buildGraph(PiServer.operation, [ColorSensor.distance, MotorDriver.turnOff])
	CFC.buildGraph(Direction.calcWeights, [ColorSensor.distance, PiServer.operation])
	CFC.buildGraph(MotorDriver.drive, [Direction.calcWeights])

	print CFC

def mission():
	#this is an example of how I think the variable class should be used.
	
	#Basic paradigm would be to create a *D variable (duplication) after every initialization.

	motors = MotorDriver()
	motorsD = Variable(motors)
	
	colorSensor = ColorSensor()
	colorSensorD = Variable(colorSensor)
	
	direction = Direction()
	directionD = Variable(direction)
	
	server = PiServer()
	serverD = Variable(server)
	
	#final point of emphasis, if we want to apply a method to both members, we can hopefully not use this
	#server.keyExchange()
	
	#but something like this instead
	serverD.assignObject(keyExchange())
	
	#I don't know if this works, but please check this
	

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
	buildControlGraph()
	mission()
