from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import RPi.GPIO as GPIO

from control import *

class MotorDriver():
	baseSpeed = 50

	def __init__(self, spd = 96):			
		baseSpeed = spd
		
	def turnOff(self):
		#global CFC
		#CFC.update(MotorDriver.turnOff)
		mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)   
		mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
		mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
		mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

	def drive(self, lSpeed=baseSpeed, rSpeed=baseSpeed, lDir = Adafruit_MotorHAT.FORWARD, rDir = Adafruit_MotorHAT.FORWARD):
		global CFC
		CFC.update(MotorDriver.drive)
		
		fl.setSpeed(lSpeed)
		bl.setSpeed(lSpeed)
		fr.setSpeed(rSpeed)
		br.setSpeed(rSpeed)

		fl.run(lDir)
		bl.run(lDir)
		fr.run(rDir)
		br.run(rDir)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

mh = Adafruit_MotorHAT(addr=0x60)

fl = mh.getMotor(1)
fr = mh.getMotor(2)
bl = mh.getMotor(3)
br = mh.getMotor(4)
		