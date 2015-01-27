from motors import *
from lightsensor import *
import threading

def drive(motors, lightsensors):
	direction = lightsensors.getAdjDirection()
	threading.Thread(target=motors.move, args=(direction,))
	t.start()
	#any other work we need to do in the foreground

	#end foreground work
	t.join()



def main():
	motors = MotorDriver()
	lightsensors = LightSensor()

	try:
		while(True):
			drive(motors, lightsensors)
	except Exception, e:
		print e
		raise e

if __name__ == '__main__':
	main()

