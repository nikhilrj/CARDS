import RPi.GPIO as GPIO
import sys,tty,termios,time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(29, GPIO.IN)
GPIO.setup(31, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(16, GPIO.IN)

pin11 = 0
pin13 = 0
pin15 = 0
pin16 = 0
pin18 = 0
pin22 = 0
pin29 = 0
pin31 = 0

count = float(0)

while(True):
	if(count < 1000):
		pin11 += GPIO.input(11)
		pin13 += GPIO.input(13) 
		pin15 += GPIO.input(15)
		pin16 += GPIO.input(16) 
		pin18 += GPIO.input(18)
		pin22 += GPIO.input(22) 
		pin29 += GPIO.input(29)
		pin31 += GPIO.input(31) 
		count += 1
	else:
		print pin11, pin13, pin15, pin16, pin18, pin22, pin29, pin31
		count = 0
		pin11 = 0
		pin13 = 0
		pin15 = 0
		pin16 = 0
		pin18 = 0
		pin22 = 0
		pin29 = 0
		pin31 = 0


	
