import RPi.GPIO as GPIO
import sys,tty,termios,time
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)   
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

fl = mh.getMotor(1)
fr = mh.getMotor(2)
bl = mh.getMotor(3)
br = mh.getMotor(4)

motors = [fl, fr, bl, br]


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(4, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

baseSpeed = 50

def sensorRead():
	#returns sensor read data as an array
	return [GPIO.input(4), GPIO.input(17), GPIO.input(27), GPIO.input(22), GPIO.input(23), GPIO.input(24)]


def calcWeights(sensorData, c=16):
	weights = [-12, -6, 0, 0, 6, 12]

	numActive = 0
	for i in sensorData:
		if i > 0:
			numActive+=1

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

def driveMotors(lSpeed=baseSpeed, rSpeed=baseSpeed, lDir = Adafruit_MotorHAT.FORWARD, rDir = Adafruit_MotorHAT.FORWARD):
	fl.setSpeed(lSpeed)
	bl.setSpeed(lSpeed)
	fr.setSpeed(rSpeed)
	br.setSpeed(rSpeed)

	fl.run(lDir)
	bl.run(lDir)
	fr.run(rDir)
	br.run(rDir)

while(True):
	sensorData = sensorRead()
	print sensorData
	[lSpeed, rSpeed, lDir, rDir] = calcWeights(sensorData)
	print [lSpeed, rSpeed]
	driveMotors(lSpeed, rSpeed, lDir, rDir)
	#time.sleep(.5)
