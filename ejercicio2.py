'''
-----------------------------
 EJERCICIO N°2
 Las excepciones son clases
-----------------------------
'''
try:
  i = int("Hola!")
except Exception as e:
  print(e)
  print(e.__str__())

'''
# ÁRBOL DE JERARQUÍA
def printArbolExc(estaClase, nivel = 0):
  if nivel > 1:
    print("   |" * (nivel - 1), end="")
  if nivel > 0:
    print("   +---", end="")

  print(estaClase.__name__)

  for subclase in estaClase.__subclasses__():
    printArbolExc(subclase, nivel + 1)

printArbolExc(BaseException)
 
# ANATOMÍA DE LAS EXCEPCIONES
def printargs(args):
	long = len(args)
	if long == 0:
		print("")
	elif long == 1:
		print(args[0])
	else:
		print(str(args))

try:
	raise Exception
except Exception as e:
	print(e.__str__(),end=' : ')
	printargs(e.args)

try:
	raise Exception("mi excepción")
except Exception as e:
	print(e.__str__(), end=' : ')
	printargs(e.args)

try:
	raise Exception("mi", "excepción")
except Exception as e:
	print(e.__str__(), end=' : ')
	printargs(e.args)
'''