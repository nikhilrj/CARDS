#Mission.py handles all overhead mission operation
from control import *

from motors import *
from color import *
from server import *
from direction import *

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


class Mission():
	def __init__(self):
		self.motors = MotorDriver()
		self.colorSensor = ColorSensor()
		self.direction = Direction()
		self.server = PiServer()
		self.server.keyExchange()

		self.target = 'blue'

		atexit.register(motors.turnOff)

	def run(self, mission2):
		#Hardware reads
		sensorData = self.direction.sensorRead()
		colorReading = self.colorSensor.readColor()


		color = __assign__(self.colorSensor.distance(colorReading))

		serverInput = self.server.operation()
		if serverInput != None:
			self.target = serverInput

		if color == self.target:
			#color handle
			exit()
		
		[lSpeed, rSpeed, lDir, rDir] = __assign__(self.direction.calcWeights(sensorData))
		self.motors.drive(lSpeed, rSpeed, lDir, rDir)

	def __assign__(self, *args, fnc):
		call = [fnc(*args), fnc(*args)]
		if __assert__(call):
			return call[0]

	def __assert__(self, var):
		assert(var[0] == var[1])

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

			
if __name__ == '__main__':
	buildControlGraph()
	mission = Variable(Mission())

	while(True):
		try:
			mission.member.run()
		except ZeroDivisionError, e:
			pass
		except (MemoryDuplicationException, ControlFlowException), e:
			pass
		except Exception, e:
			print e
			raise e

	mission.assertEquals()


