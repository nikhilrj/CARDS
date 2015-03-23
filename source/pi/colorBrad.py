import smbus
import time
bus = smbus.SMBus(1)
i2cAdr = 0x30;

# I2C address i2cAdr
# Register 0x12 has device ver. 
# Register addresses must be OR'ed with 0x80
bus.write_byte(i2cAdr,0x80|0x12)
ver = bus.read_byte(i2cAdr)
# version # should be 0x44
if ver == 0x44:
 print "Device found\n"
 bus.write_byte(i2cAdr, 0x80|0x00) # 0x00 = ENABLE register
 bus.write_byte(i2cAdr, 0x01|0x02) # 0x01 = Power on, 0x02 RGB sensors enabled
 bus.write_byte(i2cAdr, 0x80|0x14) # Reading results start register 14, LSB then MSB
 while True:
  data = bus.read_i2c_block_data(i2cAdr, 0)
  clear = clear = data[1] << 8 | data[0]
  red = data[3] << 8 | data[2]
  green = data[5] << 8 | data[4]
  blue = data[7] << 8 | data[6]
  crgb = "C: %s, R: %s, G: %s, B: %s\n" % (clear, red, green, blue)
  print crgb
  time.sleep(1)
else: 
 print "Device not found\n"