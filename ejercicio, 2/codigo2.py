#Programa No. 2: Dados tres números enteros, determinar cuál de ellos es el mayor.

import math


print("----------------------")
print("---#Programa No. 2:---")
print("----------------------")

#INPUT
n=input("Digite el primer numero : ")
n2=input("Digite el segundo numero : ")
n3=input("Digite el tercer numero : ")
n=int(n)
n2=int(n2)
n3=int(n3)

#PROCESAMIENTO
if n > n2:
    if n > n3:
        mayor=n
    else:
        mayor=n3
else:
    if n2>n3:
        mayor=n2
    else:
        mayor=n3
    #OUTPUT
    print("El numero mayor es "+str(mayor))
