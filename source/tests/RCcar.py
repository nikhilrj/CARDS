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

fl = mh.getMotor(1)
fr = mh.getMotor(2)
bl = mh.getMotor(3)
br = mh.getMotor(4)

motors = [fl, fr, bl, br]

def 

while(True):
    control=raw_input()

    if (control == "a"):
        fl.run(Adafruit_MotorHAT.BACKWARD)
        bl.run(Adafruit_MotorHAT.BACKWARD)
        fr.run(Adafruit_MotorHAT.FORWARD)
        br.run(Adafruit_MotorHAT.FORWARD)


    
    if (control == "d"):
        fl.run(Adafruit_MotorHAT.FORWARD)
        bl.run(Adafruit_MotorHAT.FORWARD)
        fr.run(Adafruit_MotorHAT.BACKWARD)
        br.run(Adafruit_MotorHAT.BACKWARD)


    if (control == "w"):
        for i in motors:
            i.run(Adafruit_MotorHAT.FORWARD)

	
    
    if (control == "s"):
        for i in motors:
            i.run(Adafruit_MotorHAT.BACKWARD)

    
    if (control == "q"):    
 #       GPIO.output(3,False)#LED
        sys.exit("Bye!")

    for i in motors:
        i.setSpeed(100)
     
    time.sleep(1.5)


    for i in motors:
        i.run(Adafruit_MotorHAT.RELEASE)
        i.setSpeed(0)