#color.py handles color detection and selection

#whiteAverage:	[52000, 16000, 19350, 12000]

#redaverage:	[16800, 9500, 3100, 3450]

#blueaverage[19000, 3800, 6300, 7500]

#greenaverage[26000, 5400, 11000, 6800]

#blackaverage[3500, 1000, 1300, 800]


import smbus, time

class ColorSensor():
#class for encapsulating color operations

	def __init__(self, whiteThreshold = 25000, blackThreshold = 5000):
		self.bus = smbus.SMBus(1);
		self.i2cAdr = 0x29;
		self.blackThreshold = blackThreshold;
		self.whiteThreshold = whiteThreshold;
		bus.write_byte(self.i2cAdr,0x80|0x12)
		ver = bus.read_byte(i2cAdr)

		if ver == 0x44:
			print "Device found\n"
			bus.write_byte(self.i2cAdr, 0x80|0x00) # 0x00 = ENABLE register
			bus.write_byte(self.i2cAdr, 0x01|0x02) # 0x01 = Power on, 0x02 RGB sensors enabled
			bus.write_byte(self.i2cAdr, 0x80|0x14) # Reading results start register 14, LSB then MSB

	def readColor(self):
		data = self.bus.read_i2c_block_data(self.i2cAdr, 0)
		clear = clear = data[1] << 8 | data[0]
		red = data[3] << 8 | data[2]
		green = data[5] << 8 | data[4]
		blue = data[7] << 8 | data[6]
		return [clear, red, green, blue]
	
	def distance(self, colorReading):
		color = ''
		if (colorReading[0] < blackThreshold):
			color = 'black'
		elif (colorReading[0] > whiteThreshold):
			color = 'white'
		else:
			if ((colorReading[1] > colorReading[3])&&(colorReading[1] > colorReading[2])):
				color = 'red'
			elif((colorReading[2] > colorReading[1])&&(colorReading[2] > colorReading[3])
				color = 'green'
			elif((colorReading[3] > colorReading[1])&&(colorReading[3] > colorReading[2])
				color = 'blue'	
			else:
				color = 'blue'
		return color