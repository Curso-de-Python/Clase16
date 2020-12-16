'''
-----------------------------
 EJERCICIO N°6
 La sentencia yield
-----------------------------
'''
# CONSTRUCCIÓN DE UN GENERADOR
def fun(n):
  for i in range(n):
    yield i

for v in fun(5):
  print(v)

'''
# ---------------------------
# GENERADOR DE POTENCIAS DE 2
def potenciasDe2(n):
  potencia = 1
  for i in range(n):
    yield potencia
    potencia *= 2

for v in potenciasDe2(8):
  print(v)

# También puedes usar listas de comprensión...
t = [x for x in potenciasDe2(5)]
print(t)

# ...convertir los valores generados en lista...
t = list(potenciasDe2(3))
print(t)

# ... y utilizar el operador in
for i in range(20):
  if i in potenciasDe2(4):
    print(i)

# ---------------------------
# GENERADOR DE NÚMEROS FIBONACCI
def Fib(n):
  p1 = p2 = 1
  for i in range(n):
    if i in [0, 1]:
      yield 1
    else:
      n = p1 + p2
      p1, p2 = p2, n
      yield n

fibs = list(Fib(10))
print(fibs)
'''