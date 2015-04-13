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
		if(self.var1.__dict__ != self.var2.__dict__)
			raise MemoryDuplicationException(str(self.var1) + 'does not equal ' + str(self.var2))
	
	
	def equateObjects(self,other)
		return self.__dict__ == other.__dict__
		
	def assign(self, argument):
		var1 = argument;
		var2 = deepcopy(argument);		
		self.assertEquals()

	def __str__(self):
		return ('var1: '+ str(self.var1) + '\n' + 'var2: '+ str(self.var2))
