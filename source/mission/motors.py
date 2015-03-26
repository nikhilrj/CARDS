from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import RPi.GPIO as GPIO

class MotorDriver():
	mh = Adafruit_MotorHAT(addr=0x60)
	baseSpeed = 50

	def __init__(self, spd = 50):			
		baseSpeed = spd

		self.fl = mh.getMotor(1)
		self.fr = mh.getMotor(2)
		self.bl = mh.getMotor(3)
		self.br = mh.getMotor(4)

		self.motors = [fl, fr, bl, br]
		
	def turnOffMotors(self):
		mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)   
		mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
		mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
		mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

	def driveMotors(self, lSpeed=baseSpeed, rSpeed=baseSpeed, lDir = Adafruit_MotorHAT.FORWARD, rDir = Adafruit_MotorHAT.FORWARD):
		fl.setSpeed(lSpeed)
		bl.setSpeed(lSpeed)
		fr.setSpeed(rSpeed)
		br.setSpeed(rSpeed)

		fl.run(lDir)
		bl.run(lDir)
		fr.run(rDir)
		br.run(rDir)

	#atexit.register(turnOffMotors)
