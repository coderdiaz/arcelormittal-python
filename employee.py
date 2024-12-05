class Person:
  def __init__(self, first_name, last_name):
    self.fname = first_name
    self.lname = last_name

class Employee(Person):
  all_employees = []

  def __init__(self, first_name, last_name, emp_id):
    Person.__init__(self, first_name, last_name)
    self.employee_id = emp_id
    Employee.all_employees.append(self)

person_1 = Person('Jorge', 'Campos')

employee_1 = Employee('Jack', 'Black', '123')
print(person_1.fname, person_1.lname)
print(employee_1.fname, employee_1.lname)

print(employee_1.all_employees)
