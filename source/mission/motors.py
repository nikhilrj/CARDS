from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import RPi.GPIO as GPIO

mh = Adafruit_MotorHAT(addr=0x60)

class MotorDriver():
	baseSpeed = 50

	def __init__(self, spd = 96):			
		baseSpeed = spd

		self.fl = mh.getMotor(1)
		self.fr = mh.getMotor(2)
		self.bl = mh.getMotor(3)
		self.br = mh.getMotor(4)

		self.motors = [self.fl, self.fr, self.bl, self.br]
		
	def turnOff(self):
		mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)   
		mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
		mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
		mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

	def drive(self, lSpeed=baseSpeed, rSpeed=baseSpeed, lDir = Adafruit_MotorHAT.FORWARD, rDir = Adafruit_MotorHAT.FORWARD):
		self.fl.setSpeed(lSpeed)
		self.bl.setSpeed(lSpeed)
		self.fr.setSpeed(rSpeed)
		self.br.setSpeed(rSpeed)

		self.fl.run(lDir)
		self.bl.run(lDir)
		self.fr.run(rDir)
		self.br.run(rDir)
