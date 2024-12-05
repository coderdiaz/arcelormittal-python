animals = {
  "birds": {
    "parrot": { "name": "Parrot", "speed": 12, "color": "yellow" },
    "grackle": { "name": "Grackle", "speed": 10, "color": "black" }
  },
  "felines": {
    "jaguar": { "name": "Jaguar", "speed": 80, "color": "yellow" },
    "lion": { "name": "Lion", "speed": 60, "color": "orange" }
  }
}

# print(type(animals))
# print(animals)

# print(animals["birds"]['parrot'])
# print(animals['sea'])

# print(animals.get("birds"))

# list_animals = list(animals)
# print(list_animals)

# for animal_type in list_animals:
#   print(animal_type)
#   # print(animals[animal_type])
#   print(animals.get(animal_type))

# birds = animals.get("birds")
# felines = animals.get("felines")

# sub_animals = (animals.get("birds", {})).get("parrot", {}).get('inhabit', 'not found')
# print(sub_animals)


animals["sea"] = {
  "whale": { "name": "Whale", "speed": 40, "color": "blue/white" },
  "shark": { "name": "Shark", "speed": 60, "color": "white"}
}

# print(animals)

# animals["felines"]["jaguar"]["speed"] = 65

# print('original', animals)

# pop

# deleted_dict = animals.pop('felines')
# print('deleted', deleted_dict)

# print('new', animals)

# prueba = animals.pop('esta_clave_no_existe', "Unknown")
# print(prueba)

# del animals['felines']
# print(animals)

# del animals['clave_no_existente']


# for key in animals:
#   print(key)
#   print(animals[key])

keys = ['birds', 'sea']
for key, value in animals.items():
  if key in keys:
    print(value)
  else:
    print('Not required')