'''
-----------------------------
 EJERCICIO N°9
 Cierres
-----------------------------
'''
def exterior(par):
	loc = par
	def interior():
		return loc
	return interior

var = 1
fun = exterior(var)
print(fun())

'''
# CIERRE CON ARGUMENTOS
def crearcierre(par):
	loc = par
	def potencia(p):
		return p ** loc
	return potencia

fsqr = crearcierre(2)
fcub = crearcierre(3)
for i in range(5):
	print(i, fsqr(i), fcub(i))
'''