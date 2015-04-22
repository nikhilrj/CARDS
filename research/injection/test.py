import inspect
import sys

#from test2 import *
class test():
	def __init__(self):
		self.a = 2
		print self
		print sys.getsizeof(self)


	def doStuff(self):
		print 'hello'

		print inspect.stack()[0][3]

		#print globals()
		global abcd 
		abcd = -1
		print globals()

		for i in globals().keys():
			if inspect.isclass(globals()[i]):
				print i, inspect.getmembers(globals()[i])
				for j in globals().values():
					if isinstance(j, globals()[i]):
						j[-1][1]()


