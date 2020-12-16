'''
-----------------------------
 EJERCICIO N°7
 Más sobre comprensión de lista
-----------------------------
'''
listaUno = []

for x in range(6):
  listaUno.append(10 ** x)

listaDos = [10 ** x for x in range(6)]

print(listaUno)
print(listaDos)

'''
# CON CONDICIONES
lista3 = []

for x in range(10):
  lista3.append(1 if x % 2 == 0 else 0)

print(lista3)

lista4 = [1 if x % 2 == 0 else 0 for x in range(10)]

print(lista4)

# CÓMO CONVERTIR UNA LISTA EN UN GENERADOR
lista = [1 if x % 2 == 0 else 0 for x in range(10)]
generador = (1 if x % 2 == 0 else 0 for x in range(10))

for v in lista:
  print(v, end=" ")
print()

for v in generador:
  print(v, end=" ")
print()

lambda parámetros: expresión
'''