#Mission.py handles all overhead mission operation
from control import *
from variable import *

from motors import *
from color import *
from server import *
from direction import *

import os, atexit, time, atexit

def buildControlGraph():
	global CFC
	CFC.buildGraph(Direction.sensorRead, [None, MotorDriver.drive, Direction.calcWeights])
	CFC.buildGraph(ColorSensor.readColor, [Direction.sensorRead]) 
	CFC.buildGraph(ColorSensor.distance, [ColorSensor.readColor, ColorSensor.distance])
	CFC.buildGraph(PiServer.operation, [ColorSensor.distance, MotorDriver.turnOff])
	CFC.buildGraph(Direction.calcWeights, [ColorSensor.distance, PiServer.operation, Direction.calcWeights])
	CFC.buildGraph(MotorDriver.drive, [Direction.calcWeights])

	print CFC


class Mission():
	def __init__(self):
		self.motors = MotorDriver()
		self.colorSensor = ColorSensor()
		self.direction = Direction()
		self.server = PiServer()
		self.server.keyExchange()

		self.target = 'blue'

		atexit.register(self.motors.turnOff)

	def run(self):
		#Hardware reads
		sensorData = self.direction.sensorRead()
		colorReading = self.colorSensor.readColor()

		color = self.__assign__(self.colorSensor.distance, colorReading)
	
		serverInput = self.server.operation()
		if serverInput != None:
			self.target = serverInput

		if color == self.target:
			#color handle
			exit()
		
		[lSpeed, rSpeed, lDir, rDir] = self.__assign__(self.direction.calcWeights, sensorData)
		self.motors.drive(lSpeed, rSpeed, lDir, rDir)

	def __assign__(self, fnc, *args):
		call = [fnc(*args), fnc(*args)]
		if self.__assert__(call):
			return call[0]

	def __assert__(self, var):
		if var[0] == var[1]:
			return True
		else:
			return False

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

			
if __name__ == '__main__':
	buildControlGraph()
	mission = Variable(Mission())
	#mission = Mission()
	#mission.member().colorSensor.connect()

	while(True):
		try:
			#mission.run()
			mission.member().run()
		except ZeroDivisionError, e:
			#print e
			pass
		#except (MemoryDuplicationException, ControlFlowException), e:
		#	print e
		#	pass
		#except Exception, e:
		#	print e
		#	raise e

	#mission.assertEquals()


