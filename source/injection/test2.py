import copy

class b():
	def __init__(self, d=5):
		self.c = d

	def inc(self):
		self.c += 1

	def __repr__(self):
		return str(self.c)

class test2():
	def __init__(self):
		self.a=3
		self.b = b()

	def doThings(self):
		self.b.inc()

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

abcd = 2332

t2 = test2()
t2c = copy.deepcopy(t2)

print t2 == t2c
t2.doThings()

print t2.__dict__, t2c.__dict__

print t2 == t2c