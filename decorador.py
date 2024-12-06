# def saludar():
#   print('Hola')

# def super_funcion(funcion):
#   funcion()

# funcion = saludar

# super_funcion(funcion)

# Decorador
# Es una funcion la cual toma como entrada
# otra funcion y a su vez retorna otra funcion.
#
# a(b) -> c

# def funcion_a(funcion_b):
#   def funcion_c():
#     print('Inicio del decorador')
#     funcion_b()
#     print('Fin del decorador')
#   return funcion_c

def funcion_a(funcion_b):
  def funcion_c(*args):
    print(*args)
    print('Inicio del decorador')
    funcion_b(*args)
    print('Fin del decorador')
  return funcion_c


@funcion_a
def saludar(a, b):
  print('Hola mundo', a, b)

saludar(1, 2)
