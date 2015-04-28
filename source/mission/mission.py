#Mission.py handles all overhead mission operation
from control import *
from variable import *

from motors import *
from color import *
from server import *
from direction import *

import os, atexit, time, atexit
from collections import Counter

def buildControlGraph():
	global CFC
	CFC.buildGraph(Direction.sensorRead, [None, MotorDriver.drive, Direction.calcWeights, PiServer.operation])
	CFC.buildGraph(ColorSensor.readColor, [Direction.sensorRead, ColorSensor.readColor, ColorSensor.distance]) 
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

		atexit.register(self.motors.turnOff)

	def run(self):
		global target
		#Hardware reads
		sensorData = self.direction.sensorRead()

		#colorReading = self.colorSensor.readColor()
		#color = self.__assign__(self.colorSensor.distance, colorReading)
		colorReadings = []
		for i in xrange(0,5):
			#print self.colorSensor.readColor()
			colorReadings.append(self.colorSensor.distance(self.colorSensor.readColor()))

		color = Counter(colorReadings).most_common(1)[0][0]
	
		serverInput = self.server.operation()
		if serverInput != None:
			target = serverInput

		if color == target:
			print 'Found target ', target, color
			#color handle
			self.motors.turnOff()
			return
		#print target,color, sensorData# colorReadings
		[lSpeed, rSpeed, lDir, rDir] = self.__assign__(self.direction.calcWeights, sensorData, clr=color)
		self.motors.drive(lSpeed, rSpeed, lDir, rDir)

	def __assign__(self, fnc, *args, **kwargs):
		call = [fnc(*args, **kwargs), fnc(*args, **kwargs)]
		if self.__assert__(call):
			return call[0]
		else:
			raise MemoryDuplicationException(str(fnc) + ' produced conflicting output')

	def __assert__(self, var):
		if var[0] == var[1]:
			return True
		else:
			return False

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	def __ne__(self, other):
		return not self.__eq__(other)

	def __repr__(self):
		return self.__dict__.__str__()

	def __hash__(self):
		return self.__repr__().__hash__()

def cfcexcepthook(exctype, value, traceback):
	if exctype == ControlFlowException:
		global mission
		mission.member().server.send(value)
		print 'Control flow exception detected'
	else:
		sys.__excepthook__(exctype, value, traceback)

			
if __name__ == '__main__':
	global mission

	buildControlGraph()
	print os.getpid()

	sys.excepthook = cfcexcepthook

	while(True):
		try:
			mission.member().run()
			mission.assertEquals()
		except ZeroDivisionError, e:
		#	print e
			pass
		#except ControlFlowException, e:
		#	mission.member().server.send(e)
		#	print 'Control flow exception detected'
		#	pass
		except MemoryDuplicationException, e:
			mission.member().server.send(e)
			mission.leaderElect()
			print 'Memory corruption fixed by CARDS'
		#except Exception, e:
		#	mission.member().server.send(e)
		#	print e
		#	raise e



