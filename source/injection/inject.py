from variable import *
import random

global mission
var = mission.member()

#call random function
functions = [var.direction.sensorRead, var.colorSensor.readColor, var.colorSensor.distance, var.motors.drive]
rand = random.randint(0, len(functions))
functions[rand]()

#change random variable
for i in var.__dict__.keys():
	if isinstance(var.__dict__[i], int):
		j = random.randint(0, 32)
		var.__dict__[i] ^= (1 << j)

for i in locals().keys():
	if isinstance(locals()[i], int):
		j = random.randint(0, 32)
		locals()[i] ^= (1 << j)