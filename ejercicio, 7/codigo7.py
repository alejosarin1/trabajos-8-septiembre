#Programa No. 7: Elaborar un programa para resolver una ecuación de primer grado

import math


print("----------------------")
print("---#Programa No. 7:---")
print("-solucion a la ecuacion de la forma ax + b = c")

#INPUT
a=input("Digite el valor a : ")
b=input("Digite el valor b : ")
c=input("Digite el valor c : ")


a=int(a)
b=int(b)
c=int(c)


#PROCESAMIENTO
if a != 0:
        x = (c-b)/a
        print("la solucion es :"+str(x))
else:
    if  a == 0 and  b != 0:
        print("la ecuacion no tiene solucion ")
    else:
        print("La ecuacion tiene infinitas soluciones.")
print(" ")