# HOF
# High Order Functions
#

# def suma(numero_1, numero_2):
#   return numero_1 + numero_2

# def substract(numero1, numero2):
#   return numero1 - numero2

# def operacion(val1, val2, funcion):
#   return funcion(val1, val2)

# resultado_suma = operacion(3, 4, suma)
# resultado_resta = operacion(3, 4, substract)

# print(resultado_suma)
# print(resultado_resta)

def crear_funcion(operador):
  if operador == '+':
    def suma(val1, val2):
      return val1 + val2
    return suma
  elif operador == '-':
    def substract(val1, val2):
      return val1 - val2
    return substract
  else:
    print('NOTHING')

def operacion(val1, val2, funcion):
  return funcion(val1, val2)


funcion_a_ejecutar = crear_funcion('-')
resultado = operacion(10, 20, funcion_a_ejecutar)
print(resultado)
