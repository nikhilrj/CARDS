import RPi.GPIO as GPIO
import sys,tty,termios,time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(27, GPIO.IN)

pin4 = 0
pin17 = 0
pin18 = 0
pin27 = 0
pin22 = 0
pin23 = 0
pin24 = 0

count = float(0)

while(True):
	if(count < 1000):
		pin4 += GPIO.input(4)
		pin17 += GPIO.input(17) 
		pin18 += GPIO.input(18)
		pin27 += GPIO.input(27) 
		pin22 += GPIO.input(22) 
		pin23 += GPIO.input(23)
		pin24 += GPIO.input(24) 
		count += 1
	else:
		print pin4, pin17, pin18, pin27, pin22, pin23, pin24
		count = 0
		pin4 = 0
		pin17 = 0
		pin18 = 0
		pin27 = 0
		pin22 = 0
		pin23 = 0
		pin24 = 0


	
