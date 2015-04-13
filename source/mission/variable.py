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
		if(self.var1 != self.var2)
			raise MemoryDuplicationException(str(self.var1) + 'does not equal ' + str(self.var2))
	
	def assertEqualsObject(self):
		if(self.var1.__dict__ != self.var2.__dict__)
			raise MemoryDuplicationException(str(self.var1) + 'does not equal ' + str(self.var2))
	
	
	def equateObjects(self,other)
		return self.__dict__ == other.__dict__
	
	#let's you assign singular variables as a pose to objects with multiple attributes	
	def assign(self, argument):
		var1 = argument;
		var2 = deepcopy(argument);		
		self.assertEquals()
		
	#Lets you use an object method with arbitrary number of args for assigning
	def assignObject(self, function, *args):
		self.var1.function(*args)
		self.var2.function(*args)
		self.assertEquals()

	def __str__(self):
		return ('var1: '+ str(self.var1) + '\n' + 'var2: '+ str(self.var2))
