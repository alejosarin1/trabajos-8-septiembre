#Programa No. 4: Construir un programa que lea un número entero y que determine si si último dígito es un número par.

import math


print("----------------------")
print("---#Programa No. 4:---")
print("----------------------")

#INPUT
n=input("Digite un numero entero  : ")
n=int(n)

#PROCESAMIENTO
if n%2 == 0:
    #OUTPUT
    print("El último dígito es un número par")
else:
    #OUTPUT
    print("El último dígito NO es un número par")
