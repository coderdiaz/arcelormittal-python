# Sets
# Mutables
# Desordenados

# Soportan:
# - Iteración a traves de for
# - Verificación de elementso via in y not in
# - Calculos de tamaño a través de len()

# No soporta
# - Acceso por indice
# - No se puede ordenar
# - Slices
# - Tampoco se pueden concatenar: +

# new_set =  {'one', 'two', frozenset({ 'three', 'four'})}
# print(type(new_set))
# print(new_set)

# Constructor
# new_set_constructor = set()

# filled_set = set([1, 2, 3, 4, 5, 6, 3, 5, 8 ,10, 3, 20])
# print(filled_set)

# numbers = [1,2,3,4,5,6,6,5,4,8,9,9,9,2,3,12,18]

# print({item ** 2 for item in numbers if item % 3 == 0})

elements_string = set('Lazaro Cardenas')
print(elements_string)