#Programa No. 8: Elaborar un programa que obtenga las raíces de una ecuación de segundo grado

import math


print("----------------------")
print("---#Programa No. 8:---")
print("-----Las raíces de una ecuación ax2 + bx + c=0------------")

#INPUT
a=input("Digite el valor a : ")
b=input("Digite el valor b : ")
c=input("Digite el valor c : ")


a=int(a)
b=int(b)
c=int(c)
#PROCESAMIENTO
if a*c<0:
    print("")
    x1=(-b-math.sqrt((b**2)-4*a*c))
    x1=x1/(2*a)
    print("x1 :"+str(x1))
    print("")
    x2=(-b+math.sqrt((b**2)-4*a*c))
    x2=x2/(2*a)
    print("x2 :"+str(x2))

else:
    print("")
    print("la ecuacion no tiene solucion en los reales:")
