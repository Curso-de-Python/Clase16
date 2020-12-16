'''
-----------------------------
 EJERCICIO N°3
 Creando tus propias excepciones
-----------------------------
'''
class MyZeroDivisionError(ZeroDivisionError):	
	pass

def hazLaDivision(mine):
	if mine:
		raise MyZeroDivisionError("peores noticias")
	else:		
		raise ZeroDivisionError("malas noticias")

for modo in [False, True]:
	try:
		hazLaDivision(modo)
	except ZeroDivisionError:
		print('División entre cero')

for modo in [False, True]:
	try:
		hazLaDivision(modo)
	except MyZeroDivisionError:
		print('Mi división entre cero')
	except ZeroDivisionError:
		print('División entre cero original')