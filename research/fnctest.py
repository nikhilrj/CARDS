import traceback

def fnc1():
	#assert a[current_fnc] == prev_fnc
	#print 'hi'
	fnc2()

def fnc2():

	traceback.print_stack()
	print 'bye'

a = {}
a[fnc1] = fnc2
print a
fnc1()
