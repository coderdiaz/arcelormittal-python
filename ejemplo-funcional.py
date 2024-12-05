# Map
#
# map(funcion a aplicar, objeto iterable)

# Calcular el cuadrado de todos los elementos
# def cuadrado(elemento):
#   return elemento ** 2

# elementos = list((1, 2, 3, 4, 5, 6,))

# # mapped_values = map(cuadrado, elementos)
# # print(type(mapped_values))

# resultado = list(map(cuadrado, elementos))

# print(resultado)




# Filter
#
# filter(funcion, objeto iterable)

# def mayor_a_cinco(elemento):
#   return elemento > 5

# tupla = (5, 2, 6, 7, 10, 77, 2, 30, 4, 2,)

# wtf = filter(mayor_a_cinco, tupla)
# print(type(wtf))

# resultado = tuple(filter(mayor_a_cinco, tupla))
# print(resultado)



# Reduce
#
# reduce(funcion, objeto iterable)
#

# Obtener la suma de todos numeros de una lista

# lista = [1, 2, 3, 4, 5, 6]
# acumulador = 0

# for elemento in lista:
#   acumulador += elemento

# print(acumulador)

from functools import reduce

lista = [1, 2, 3, 4, 5, 6]

# def func_acumulador(acumulador = 0, elemento = 0):
#   return acumulador + elemento

# resultado = reduce(func_acumulador, lista)

resultado = reduce(lambda acc = 0, el = 0 : acc + el, lista)
print(resultado)
