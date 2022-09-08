#Programa No. 3: Construir un programa que lea un número entero y determine si es un número positivo de 4 dígitos


import math


print("----------------------")
print("---#Programa No. 3:---")
print("----------------------")

#INPUT
n=input("Digite un numero entero  : ")
n=int(n)

#PROCESAMIENTO
n=n//1000
if 10>n>0:
    print("El numero  de 4 digitos")
else:
    print("El numero NO tiene 4 digitos")

    
