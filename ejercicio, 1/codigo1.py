#Programa No. 4: Ingresar el tiempo de duración de una llamada telefónica y determinar la cantidad a pagar, de acuerdo con lo siguiente:

#a. Toda llamada que dure tres minutos o menos tienen un costo de $300.
#b. Cada minuto adicional cuesta $50.

import math


print("----------------------")
print("---#Programa No. 1:---")
print("----------------------")

#INPUT
n=input("Digite la duracion de la llamada : ")
n=int(n)

#PROCESAMIENTO
if n <= 3:
    #OUTPUT
    print("La llamada tiene un costo de: 300$")
else:
    r=((n-3)*50)+300
    #OUTPUT(2)
    print("La llamada tiene un costo de: "+str(r)+"$")
