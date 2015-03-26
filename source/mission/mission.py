#Mission.py handles all overhead mission operations.


from motors import *
from color import *
from server import *
from direction import *

import os, atexit, time


def sensorRead():
	#returns sensor read data as an array
	return [GPIO.input(17), GPIO.input(18), GPIO.input(27), GPIO.input(22), GPIO.input(23), GPIO.input(24)]


while(True):
	#Make calls to other files
	
	

