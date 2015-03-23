import RPi.GPIO as GPIO
import sys,tty,termios,time
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit

import os

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

baseSpeed = 48

#color sensor read
import smbus, time
bus = smbus.SMBus(1)
i2cAdr = 0x29;

bus.write_byte(i2cAdr,0x80|0x12)
ver = bus.read_byte(i2cAdr)

if ver == 0x44:
	print "Device found\n"
	bus.write_byte(i2cAdr, 0x80|0x00) # 0x00 = ENABLE register
	bus.write_byte(i2cAdr, 0x01|0x02) # 0x01 = Power on, 0x02 RGB sensors enabled
	bus.write_byte(i2cAdr, 0x80|0x14) # Reading results start register 14, LSB then MSB

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
	
def readColor():
	data = bus.read_i2c_block_data(i2cAdr, 0)
	clear = clear = data[1] << 8 | data[0]
	red = data[3] << 8 | data[2]
	green = data[5] << 8 | data[4]
	blue = data[7] << 8 | data[6]
	return [clear, red, green, blue]

def distance(colorReading):
	colors = {}
	colors['black'] = [ 4000, 900, 1500, 1047]
	colors['red'] = [ 15000, 10000, 2600, 2400]
	colors['blue'] = [ 8900, 1400, 3100, 3300 ]
	colors['green'] = [ 7000, 1100, 3000, 2000 ]
	colors['white'] = [65535, 22000, 29000, 18000]
	
	dist = 0
	mindist = 10000000
	color = ''
	for j in colors.keys():
		for i in xrange(0, len(colorReading)):
			dist += (colors[j][i]-colorReading[i])**2
		dist **= .5
		if dist < mindist:
			mindist = dist
			color = j
	return color

print os.getpid()

while(True):
	sensorData = sensorRead()
	
	colorReading = readColor()
	color =  distance(colorReading)
	if color != 'white':
		print color, colorReading
	
	#print sensorData
	try:
		[lSpeed, rSpeed, lDir, rDir] = calcWeights(sensorData)
	except ZeroDivisionError as e:
		#print e
		2+2
	
	#print [lSpeed, rSpeed]

while(True):
	sensorData = sensorRead()
	print sensorData
	try:
		[lSpeed, rSpeed, lDir, rDir] = calcWeights(sensorData)
	except:
		print 'SHIT BROKE, DOING WHAT WE DID LAST!'
	print [lSpeed, rSpeed]
	driveMotors(lSpeed, rSpeed, lDir, rDir)
	#time.sleep(.5)
