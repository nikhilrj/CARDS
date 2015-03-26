#color.py handles color detection and selection

import smbus, time


def colorInit():
	bus = smbus.SMBus(1)
	i2cAdr = 0x29;
	blackThreshold = 5000;
	whiteThreshold = 20000;

	bus.write_byte(i2cAdr,0x80|0x12)
	ver = bus.read_byte(i2cAdr)

	if ver == 0x44:
		print "Device found\n"
		bus.write_byte(i2cAdr, 0x80|0x00) # 0x00 = ENABLE register
		bus.write_byte(i2cAdr, 0x01|0x02) # 0x01 = Power on, 0x02 RGB sensors enabled
		bus.write_byte(i2cAdr, 0x80|0x14) # Reading results start register 14, LSB then MSB
	
	

def readColor():
	data = bus.read_i2c_block_data(i2cAdr, 0)
	clear = clear = data[1] << 8 | data[0]
	red = data[3] << 8 | data[2]
	green = data[5] << 8 | data[4]
	blue = data[7] << 8 | data[6]
	return [clear, red, green, blue]
	
def distance(colorReading):
	color = ''
	if (colorReading[0] < blackThreshold):
		color = 'black'
	elif (colorReading[0] > whiteThreshold):
		color = 'white'
	else:
		if (colorReading[1] > colorReading[3]):
			color = 'red'
		else:
			color = 'blue'
	return color