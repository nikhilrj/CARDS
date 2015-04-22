from copy import deepcopy
import mission
import random

class MemoryDuplicationException(Exception):
	def __init__(self,val):
		self.value = val
	
	def __str__(self):
		return repr(self.value)	

class Variable():

	def __init__(self, var, copies = 5):
		self.var = []
		self.copies = copies
		for i in xrange(0, copies):
			self.var.append(deepcopy(self.var))

	def member(self):
		return self.var[random.randint(0, self.copies - 1)]

	def assertEquals(self):
		self.equalities = {}
		for i in xrange(0, self.copies):
			try:
				self.equalities[self.var[i]] += 1
			except Exception, e:
				self.equalities[self.var[i]] = 1

		if len(self.equalities.keys())
			raise new MemoryDuplicationException('Memory Corruption Error ' + self.equalities.__str__())

	def leaderElect(self):
		votes = 0
		leader = None
		
		for i in self.equalities.keys():
			if self.equalities[i] > votes:
				votes = self.equalities[i]
				leader = i

		for i in xrange(0, self.copies):
			if var[i] != leader:
				var[i] = deepcopy(leader)

	def __str__(self):
		return str(self.var)


mission = Variable(mission.Mission())
