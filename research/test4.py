import random
def injectMemory(dic):
	for i in dic.keys():
		if isinstance(dic[i], dict):
			injectMemory(dic[i])
		if isinstance(dic[i], (int, float)):
			if random.random() > 0.95:
				dic[i] ^= (1 << random.randint(0, 32))


a = {'hi':5 , 'hey':3, 'abc':{'def':7}}

print a
injectMemory(a)
print a
