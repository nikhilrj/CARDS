import sys
import ctypes
import binascii

class a():
	def __init__(self):
		self.b = 3
	def fnc(self):
		print 'hi'

c = a()
c.fnc()
d = 5
e = 7.4

for i in globals().keys():
	if isinstance(globals()[i], (float, int)):
		print i, globals()[i], sys.getsizeof(globals()[i])
		print binascii.hexlify(ctypes.string_at(id(globals()[i]), sys.getsizeof(globals()[i])))
		ctypes.string_at(id(globals()[i]), sys.getsizeof(globals()[i])) ^= 0x01
		print binascii.hexlify(ctypes.string_at(id(globals()[i]), sys.getsizeof(globals()[i])))
		#print ctypes.string_at(id(globals()[i]), sys.getsizeof(globals()[i]))