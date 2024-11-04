#Hallar el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
factorial_5 = print(factorial(5))


#Sucesion de Fibonacci
def fibonacci(n) :
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
number = 6
print(fibonacci(number))

#Serie de fibonacci con límites
def fibonacci(f1, f2, n):

    print(f1)

    if n > f2:

        print(f2)

        fibonacci ( f1 + f2, f1 + f2 + f2 , n)

    else:

        print ("fin")

fibonacci(0,1,int(input("Generar fibonacci con limite: ")))