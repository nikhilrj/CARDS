
class ControlFlowException(Exception):
	def __init__(self, val):
		self.value = val

	def __str__(self):
		return repr(self.value)


class ControlFlowControl():
	def __init__(self):
		self.prevState = None
		self.graph = {}

	def buildGraph(self, current, previous):
		#assumes hierarchy = [[fnc1], [fnc2, fnc3], [fnc4]]
		self.graph[current] = previous

	def update(self, fnc):
		self.__isValid__(fnc)
		self.prevState = fnc

	def __isValid__(self, current):
		if current not in self.graph[self.prevState]:
			raise ControlFlowException(str(current) + ' cannot follow ' + str(self.prevState))

