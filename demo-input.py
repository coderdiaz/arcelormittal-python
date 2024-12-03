# input() es una función que permite al usuario ingresar datos

llegada = int(input('Hora de llegada (formato 24 hrs): '))
salida = int(input('Hora de salida (formato 24 hrs): '))
precio_por_hora = int(input('Precio por hora: '))

# llegada = 10
# salida = 20
# precio_por_hora = 100

total = (salida - llegada) * precio_por_hora

print(total)