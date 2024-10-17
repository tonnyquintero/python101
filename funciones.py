#funciones se inicializan con def
def greet(name, last_name="No tiene apellido"):
    print("Hola", name, last_name)

greet("Tonny", "Quintero")
greet("diego")

#Hacer una calculadora
def add(a,b):
    return a + b

def sustract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def calculator():
    while True:
        print("Seleccione una operación: ")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        option = (input("Ingresa una opción: "))

        if option == "5":
            print("Saliendo de la aplicación")
            break

        if option in ["1","2","3","4"]:
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))

            if option == "1":
                print("La suma es: ", add(num1, num2))
            elif option == "2":
                print("La resta es: ", sustract(num1, num2))
            elif option == "3":
                print("La multiplicación es: ", multiply(num1, num2))
            elif option == "4":
                print("La división es: ", divide(num1,num2))
        
        else:
            print("Opcion incorrecta")

calculator()
