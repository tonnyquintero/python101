#Los diccionarios son como objetos enjavascript {}
numbers = {1: "uno", 2: "dos", 3: "tres"}
print(numbers)
print(type(numbers))

information = {"nombre": "Anthony",
               "apellido": "Quintero",
               "edad": 33,
               "dev": True}

print(information)
del information["dev"]
print(information)
print(information["edad"])

claves = information.keys()
print(claves)
valores = information.values()
print(valores)

#diccionario de diccionarios
contacts = {"Anthony": {"apellido": "Quintero",
               "edad": 33,
               "dev": True},
            "Diego": {"apellido": "Valencia",
               "edad": 25,
               "dev": False},
            "Daniel": {"apellido": "Castillo",
               "edad": 42,
               "dev": False}}

print(contacts["Daniel"])