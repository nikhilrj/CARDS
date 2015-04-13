from copy import deepcopy

class MemoryDuplicationException(Exception):
	def __init__(self,val):
		self.value = val
	
	def __str__(self):
		return repr(self.value)	

class Variable():

	def __init__(self, var):
		self.var1 = var;
		self.var2 = deepcopy(var);

	def assertEquals(self):
		if(var1 != var2)
			raise MemoryDuplicationException(str(self.var1) + 'does not equal ' + str(self.var2))
	
	
	def assign(self, argument):
		var1 = argument;
		var2 = argument;		
		self.assertEquals()

	def __str__(self):
		return ('var1: '+ str(self.var1) + '\n' + 'var2: '+ str(self.var2))
