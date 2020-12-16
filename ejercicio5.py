'''
-----------------------------
 EJERCICIO N°5
 El protocolo iterador
-----------------------------
'''
# EJEMPLO 1
class Fib:
	def __init__(self, nn):
		print("__init__")
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1

	def __iter__(self):
		print("__iter__")		
		return self

	def __next__(self):
		print("__next__")				
		self.__i += 1
		if self.__i > self.__n:
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret

for i in Fib(10):
	print(i)

'''
# EJEMPLO 2
class Fib:
	def __init__(self, nn):
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1

	def __iter__(self):
		print("Fib iter")
		return self

	def __next__(self):
		self.__i += 1
		if self.__i > self.__n:
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret

class Clase:
	def __init__(self, n):
		self.__iter = Fib(n)

	def __iter__(self):
		print("Clase iter")
		return self.__iter;

object = Clase(8)

for i in object:
	print(i)

def fun(n):
  for i in range(n):
    yield i
'''