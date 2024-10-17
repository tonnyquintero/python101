x = 9

if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")

print("afuera del ciclo")

y = 10 
z = 25

if y>10 and z>15:
    print("y es mayor que 10 y z es mayor que 15")

if y>10 or z>25:
    print("y es mayor que 10 o z es mayor que 25")

if not y>10:
    print("y no es mayor que 10")

#if anidados
is_member = True
age = 5

if is_member:
    if age>=15:
        print("tienes acceso ya que eres miembro y tienes 15 o más años")
    else: print("no tienes acceso porque eres miembro pero no cumples con la edad")
else:
    print("no tienes acceso porque no eres miembro")