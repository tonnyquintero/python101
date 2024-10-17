#          así es su sintaxis: se crea una variable con una operacion y ya despues se cicla
squares = [x**2 for x in range(1,11)]
print("Cuadrados: ", squares)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print("Temperatura en F: ", fahrenheit)

#Numeros pares
evens = [x for x in range(1,21) if x%2 == 0]
print("Numeros pares:",evens)

#Transponer una matriz
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix)
print(transposed)