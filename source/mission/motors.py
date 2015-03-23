from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import RPi.GPIO as GPIO

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

def driveMotors(lSpeed=baseSpeed, rSpeed=baseSpeed, lDir = Adafruit_MotorHAT.FORWARD, rDir = Adafruit_MotorHAT.FORWARD):
	fl.setSpeed(lSpeed)
	bl.setSpeed(lSpeed)
	fr.setSpeed(rSpeed)
	br.setSpeed(rSpeed)

	fl.run(lDir)
	bl.run(lDir)
	fr.run(rDir)
	br.run(rDir)