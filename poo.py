# Programación Orientada a Objetos (POO)
#
# Datos -> Atributos
# Comportamiento
#
# class A:
#   attr_1 = 5
#   attr_2 = "Hello!"

# new_object = A()
# print(new_object.attr_1)
# print(new_object.attr_2)


class B:
  number = 5
  __string = "Hello!"

  def __init__(self, location):
    print(self)
    self.location_x = location[0]
    self.location_y = location[1]

  def change_location(self, amount):
    self.location_x += amount
    self.location_y += amount
    self.__protected_method()
    return self.location_x, self.location_y

  def __protected_method(self):
    print('Hello world')


new_object = B((1, 2))
print(new_object.location_x)
print(new_object.location_y)

datos = new_object.change_location(10)
new_object.__string
print(datos)
