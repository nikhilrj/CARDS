import RPi.GPIO as GPIO
import sys,tty,termios,time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Setup GPIO
GPIO.setup (5, GPIO.OUT)    
GPIO.setup (7, GPIO.OUT)      
GPIO.setup (10, GPIO.OUT)    
GPIO.setup (12, GPIO.OUT)

#Enable Signals
GPIO.setup (3, GPIO.OUT)
GPIO.output(3,True)
GPIO.setup (8, GPIO.OUT)
GPIO.output(8,True)


GPIO.output(12,True)
time.sleep(3)
GPIO.output(7, True)
GPIO.output(5, True)
time.sleep(20)

GPIO.output(7, False)
GPIO.output(5, False)
