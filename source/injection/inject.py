from variable import *
import random, time

def runCircle():
	var.motors.drive(100, 100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.FORWARD)

def runCircle2():
	var.motors.drive(100, 100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.BACKWARD)

def runFWBW():
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
		if isinstance(dic[i], dict):
			injectMemory(dic[i])
		if isinstance(dic[i], (int, float)):
			if random.random() > 0.95:
				dic[i] ^= (1 << random.randint(0, 32))

global mission
var = mission.member()

#call random function
functions = [var.direction.sensorRead, var.colorSensor.readColor, var.colorSensor.distance, var.motors.drive]
rand = random.randint(0, len(functions))
#functions[rand]()

injectMemory(var)
