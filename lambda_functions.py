add = lambda a, b: a + b

print(add(10,4))

multiply = lambda c, d: c * d
print(multiply(85,4))

#cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))
print("Cuadrados: ", squared_numbers)

#numeros pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print("numeros pares: ", even_numbers)