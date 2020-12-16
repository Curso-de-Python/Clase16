'''
-----------------------------
 EJERCICIO N°8
 La función lambda
-----------------------------
'''
# FUNCIONES LAMBDA NO ANÓNIMAS
dos = lambda : 2
cuadrado = lambda x : x * x
potencia = lambda x, y : x ** y

for a in range(-2, 3):
  print(cuadrado(a), end=" ")
  print(potencia(a, dos()))

'''
# ----------------------------
# EJEMPLO DE USO 1
# Sin lambda
def imprimirfuncion(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

def polinomio(x):
	return 2 * x**2 - 4 * x + 2

imprimirfuncion([x for x in range(-2, 3)], polinomio)

# Con lambda
def imprimirfuncion(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

imprimirfuncion([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

map(función, lista)

# ----------------------------
# EJEMPLO DE USO 2: map()
lista1 = [x for x in range(5)]
lista2 = list(map(lambda x: 2 ** x, lista1))
print(lista2)

for x in map(lambda x: x * x, lista2):
	print(x, end=' ')
print()

# ----------------------------
# LA FUNCIÓN filter()
from random import randint

data = [ randint(-10,10) for x in range(5) ]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)
print(filtered)
'''