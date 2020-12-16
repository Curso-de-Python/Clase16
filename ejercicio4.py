'''
-----------------------------
 EJERCICIO N°4
 Excepciones y pizzas
-----------------------------
'''
class PizzaError(Exception):
  def __init__(self, pizza, mensaje):
    Exception.__init__(self, mensaje)
    self.pizza = pizza	

class DemasiadoQuesoError(PizzaError):
  def __init__(self, pizza, queso, mensaje):
    PizzaError.__init__(self, pizza, mensaje)
    self.queso = queso

'''
# PRUEBA DE LAS EXCEPCIONES
def hacerPizza(pizza, queso):
	if pizza not in ['americana', 'hawaiana', 'pepperoni']:
		raise PizzaError(pizza, "No hay tal pizza en el menú")
	if queso > 100:
		raise DemasiadoQuesoError(pizza, queso, "Demasiado queso")
	print("¡Pizza lista!")

for (pz, qu) in [('pepperoni', 0), ('americana', 110), ('suprema', 20)]:
	try:
		hacerPizza(pz, qu)
	except DemasiadoQuesoError as DQE:
		print(DQE, ':', DQE.queso)
	except PizzaError as PZE:
		print(PZE, ':', PZE.pizza)

# ---------------------------
# SOLUCIÓN FINAL
class PizzaError(Exception):
  def __init__(self, pizza='desconocida', mensaje=''):
    Exception.__init__(self, mensaje)
    self.pizza = pizza

class DemasiadoQuesoError(PizzaError):
  def __init__(self, pizza='desconocida', queso='>100', mensaje=''):
    PizzaError.__init__(self, pizza, mensaje)
    self.queso = queso

def hacerPizza(pizza, queso):
	if pizza not in ['americana', 'hawaiana', 'pepperoni']:
		raise PizzaError
	if queso > 100:
		raise DemasiadoQuesoError
	print("¡Pizza lista!")

for (pz, qu) in [('pepperoni', 0), ('americana', 110), ('suprema', 20)]:
	try:
		hacerPizza(pz, qu)
	except DemasiadoQuesoError as DQE:
		print(DQE, ':', DQE.queso)
	except PizzaError as PZE:
		print(PZE, ':', PZE.pizza)
'''