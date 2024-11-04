#imprimir archivo y eliminar saltos de linea
"""with open('caperucita.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

#Leer todas las lineas en una lista
"""with open('caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)"""

#Añadir al final del archivo
with open('caperucita.txt', 'a') as file:
    file.write("\n\nWrited by ChatGPT 💜")

#Sobreescribir archivo
"""with open('caperucita.txt', 'w') as file:
    file.write("He borrado todos tus datos")"""

with open ("caperucita.txt", "r") as archivo:
    lineas = archivo.readlines()

print(len(lineas))