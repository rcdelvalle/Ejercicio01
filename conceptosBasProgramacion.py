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


#Ejercicio 6.
listanum2 = [3, 5, 7]
suma = 0
cont = 0

for num in listanum2:
    suma = suma + num
    cont += 1

if cont > 0:
    prom = suma/cont

print(f"El valor promedio de la lista es {prom}")


#Ejercicio 7.
listanum3 = [3, 5, 13, 11, 73, 59, 37]
numeroMaximo = listanum3[1]

for num in listanum3:
    if num >= numeroMaximo:
        numeroMaximo = num

print(f"El valor máximo de la lista es {numeroMaximo}")


#Ejercicio 8.
listanum4 = [1, 3, -5, 7, -11, 15]
numeroMinimo = listanum4[1]

for num in listanum4:
    if num <= numeroMinimo:
        numeroMinimo = num

print(f"El valor mínimo de la lista es {numeroMinimo}")

