from copy import deepcopy
import mission
import random

class MemoryDuplicationException(Exception):
	def __init__(self,val):
		self.value = val
	
	def __str__(self):
		return repr(self.value)	

class Variable():

	def __init__(self, var):
		self.var1 = var;
		self.var2 = deepcopy(var);

	def member(self):
		if random.random() > 0.5:
			return self.var1
		else: 
			return self.var2

	def assertEquals(self):
		if(self.var1 != self.var2):
			raise MemoryDuplicationException(str(self.var1) + '\ndoes not equal\n' + str(self.var2))

	def __str__(self):
		return ('var1: '+ str(self.var1) + '\n' + 'var2: '+ str(self.var2))

mission = Variable(mission.Mission())
