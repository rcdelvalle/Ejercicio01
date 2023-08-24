# Ejercicio 1.
numImp = (int(input("Ingrese un nro impar ")))

while ((numImp % 2) == 0):
    numImp = (int(input("Ingrese un nro impar ")))

print ("El numero ingresado es impar")


#Ejercicio 2.
print("Ingrese dos nros")
num1 = (float(input("Ingrese el primer nro ")))
num2 = (float(input("Ingrese el segundo nro " )))
print("Tiene 3 opciones (1. sumar, 2. restar y 3. multiplicar)")
opcion = (int(input("Ingrese una opcion ")))

while (opcion<1 or opcion>3):
    opcion = (int(input("Ingrese una opcion ")))    

if opcion==1:
    resultado = num1 + num2
elif opcion==2:
    resultado = num1 - num2
elif opcion==3:
    resultado = num1 * num2

print(f"El resultado es {resultado}")


#Ejercicio 3.
email = input("Ingrese un email ")
mensaje = "No es un email"

for caracter in email:
    if (caracter == "@"):
        mensaje = "Si es un email"
        break

print(mensaje)


#Ejercicio 4.
lista = ["banano", "sandía", "cereza", "higo", "melón", "manzana"]
cont = 0

for item in lista:
    cont += 1

print(f"la cantidad de elementos de la lista es {cont}")


#Ejercicio 5.
listanum = [2, 3, 5, 7, 11, 13, 17, 19]
suma = 0

for num in listanum:
    suma = suma + num

print(f"El total de la suma es {suma}")