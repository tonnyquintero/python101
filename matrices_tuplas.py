#una lista con 3 listas
matrix = [[1,2,3,],
          [4,5,6],
          [7,8,9]]

print(matrix)

#aquí imprimimos las coordenadas para el numero 6
print(matrix[1][2])

#una lista con 2 listas que tienen 3 listas
matrix_double = [[[1,2,3],
                [4,5,6],
                [7,8,9]], 
                [[10,11,12],
                [13,14,15],
                [16,17,18]]]

print(matrix_double)
#aqui imprimimos las coordenadas para el numero 15
print(matrix_double[1][1][2])

#----TUPLAS---- se encierran en parentesis y son de caracter inmutable
numbers = (20,30,40,50)
print(numbers)
print(type(numbers))
print(numbers[2])