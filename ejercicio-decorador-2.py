def decorador_con_valor(name):
  def customed_decorator(funcion):
    def wrapper(*args):
      print('name', name)
      return funcion(*args)
    return wrapper
  return customed_decorator


@decorador_con_valor('ArcelorMittal')
def suma(a,b):
  return a + b

print(suma(10, 20))
