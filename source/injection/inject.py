from variable import *
import random, time

def runCircle(var):
	var.motors.drive(150, 150, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.FORWARD)

def runCircle2(var):
	var.motors.drive(150, 150, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.BACKWARD)

def runFWBW(var):
	var.motors.drive(50, 50, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD)
	time.sleep(.5)
	var.motors.drive(50, 50, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD)
	time.sleep(.5)
	var.motors.drive(50, 50, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD)
	time.sleep(.5)
	var.motors.drive(50, 50, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD)
	time.sleep(.5)
	var.motors.drive(50, 50, Adafruit_MotorHAT.RELEASE, Adafruit_MotorHAT.RELEASE)


def injectMemory(dic):
	for i in dic.keys():
		try:
			if isinstance(dic[i], (int, float)):
				if random.random() > 0:#.95:
					print 'changing', dic[i]
					dic[i] ^= (1 << random.randint(0, 32))
			elif isinstance(dic[i], object):
				injectMemory(dic[i].__dict__)

		except Exception, e:
			print e
			pass

global mission
var = mission.member()

print var

#call random function
functions = [var.direction.sensorRead, var.colorSensor.readColor, var.colorSensor.distance, var.motors.drive]
rand = random.randint(0, len(functions)-1)
#functions[rand]()

#print 'running in circle'
#runCircle(var)

#print 'running fwbw'
#runFWBW(var)
#print 'stopped'

injectMemory(var.__dict__)
print var
