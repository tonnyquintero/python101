a = [1,2,3,4,5]
b = a
print(a)
print(b)

#lo borra de las 2 listas ya q se está es copiando el espacio en memoria 
del a[0]
print(a)
print(b)

#es el mismo id en memoria
print(id(a))
print(id(b))

#si aplicamos "slice" no copiamos el espacio en memoria y así queda independiente de las demás
c = a[:]
print(id(c))

a.append(6)
print(a)
print(b)
print(c)

#otra forma con el método copy
lista1 = ["a","b","c","d","e"]
lista2 = lista1.copy()

lista2.append( True )

print( lista1 )
print( lista2 )