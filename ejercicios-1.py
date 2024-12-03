# Ejercicio 1: Calculadora
# Crea un programa que pida al usuario dos números
# y una operación a realizar
# entre ellos (suma, resta, etc)
# Hint: Los valores de True y False se
# pueden interpretar como 1 y 0
# Hint 2: Puedes usar +=

# numero_1 = int(input('Ingrese el primer número: '))
# numero_2 = int(input('Ingrese el segundo número: '))
# operacion = input('Ingrese la operación a realizar (+, -, *, /): ')

# resultado = 0

# resultado = resultado + ((operacion == '+') * (numero_1 + numero_2))
# resultado = resultado + ((operacion == '-') * (numero_1 - numero_2))
# resultado = resultado + ((operacion == '*') * (numero_1 * numero_2))
# resultado = resultado + ((operacion == '/') * (numero_1 / numero_2))

# print(resultado)

# Ejercicio 2
# Dado 3 ángulos de un triangulo
# A, B, C, determinar si es un triangulo
# Hint: La suma de los tres ángulos internos
# es igual a 180 grados

vertice_a = int(input('Ingrese el ángulo A: '))
vertice_b = int(input('Ingrese el ángulo B: '))
vertice_c = int(input('Ingrese el ángulo C: '))

es_triangulo = (vertice_a + vertice_b + vertice_c) == 180
print("¿Es un triangulo?", str(es_triangulo))
