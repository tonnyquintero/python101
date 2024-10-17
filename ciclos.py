numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:
    print("Aquí i es igual a:",i)

for i in numbers:
    print("Aquí i sumando 2 es igual a:",i+2)

#range sintaxis = range(desde donde arranca OPCIONAL, hasta donde llega menos 1, steps o saltos OPCIONAL)
for i in range(3,20,2):
    print(i)

fruits = ["manzana", "pera", "melon", "uva", "naranja", "tomate"]
for fruit in fruits:
    print(fruit)
    if fruit == "naranja":
        print("naranja encontrada")

#ciclo while
x = 0
while x<5:
    print(x)
    x+=1

#while con break
x = 0
while x<5:
    if x == 3:
        break
    print(x)
    x+=1

#for con continue
numbers2 = [1, 2, 3, 4, 5, 6]
for i in numbers2:
    if i ==3:
        continue
    print("Aquí i es igual a:",i)