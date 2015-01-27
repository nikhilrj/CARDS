import RPi.GPIO as GPIO

class MotorDriver():
	dir_lookup = {'UP': 12, 'DOWN': 10, 'LEFT':5, 'RIGHT':7}

	def MotorDriver(self, delay=.5):
		#GPIO Mode
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)	

		#GPIO Direciton
		GPIO.setup(5, GPIO.OUT)
		GPIO.setup(7, GPIO.OUT)
		GPIO.setup(10, GPIO.OUT)
		GPIO.setup(12, GPIO.OUT)

		#GPIO Enable
		GPIO.setup(3, GPIO.OUT)
		GPIO.output(3, True)
		GPIO.setup(8, GPIO.OUT)
		GPIO.output(8, True)

		self.delay = delay

	def move(self, direction):
		GPIO.output(self.dir_lookup[direction], True)
		thread.sleep(self.delay)


