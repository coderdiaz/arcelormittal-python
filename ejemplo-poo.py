class Parent:
  def __init__(self, first_name, last_name):
    self.fname = first_name
    self.lname = last_name

class Child(Parent):
  pass


padre = Parent("Jorge", "Perez")
child = Child("Juan", "Perez")

print(padre.fname, padre.lname)
print(child.fname, child.lname)
