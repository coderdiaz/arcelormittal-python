# Tuplas
# Son inmutables
# bracket-notation [] / 0-index / -1 index

no_elements = tuple()
print(type(no_elements))
print(no_elements)

one_elements = tuple([16])
print(one_elements)

elements_string = tuple("Lazaro Cardenas")
print(elements_string)

source_data = { "fish": "gold", "monkey": "brown" }
tuple_data = tuple(source_data)
print(tuple_data)

tuple_data_dic = tuple(source_data.items())
print(tuple_data_dic)


# Literal definition
new_tuple = ()
other_tuple = (16,)
print(new_tuple, type(new_tuple))
print(other_tuple, type(other_tuple))

tupla_1 = (0,1,2,)
tupla_2 = (3,4,5,)
new_combined_tuple = tupla_1 + tupla_2
print(new_combined_tuple)

other_repeated_tuple = tupla_1 * 5
print(other_repeated_tuple)

colors = {
  'red': ('Red', 'Red 500', (59, 178, 146,), '#000'),
  'blue': ('Blue', 'Blue 500', (59, 178, 146,), '#000'),
}