'''
-----------------------------
 EJERCICIO N°1
 Más sobre excepciones
-----------------------------
'''
# RAMA ELSE
def reciproco(n):
  try:
    n = 1 / n
  except ZeroDivisionError:
    print("División fallida")
    return None
  else:
    print("Todo salió bien")
    return n

print(reciproco(2))
print(reciproco(0))

# RAMA FINALLY. Agrega:
#  finally:
#    print("Es el momento de decir adiós")
#     return n