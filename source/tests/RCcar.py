from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
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



while(True):
    control=raw_input()

    if (control == "a"):
        GPIO.output(5,True)
    
    if (control == "d"):
        GPIO.output(7,True)

    if (control == "w"):
        GPIO.output(12,True)
    
    if (control == "s"):
        GPIO.output(10,True)

    if (control == "q"):    
 #       GPIO.output(3,False)#LED
        sys.exit("Bye!")
     
    time.sleep(.5)
    GPIO.output(10,False)
    GPIO.output(12,False)
    GPIO.output(5,False)
    GPIO.output(7,False)
  #  ledstate=not ledstate
  #  GPIO.output(3,ledstate)

    
