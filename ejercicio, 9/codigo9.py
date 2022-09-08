#Programa No. 4: Construir un programa que lea un número entero y que determine si si último dígito es un número par.

import math


print("----------------------")
print("---#Programa No. :---")
print("----------------------")

#INPUT
n=input("Digite el tipo de cliente: General(G) o Afiliado(A)  : ")
v=input("Digite el monto de la compra : ")
p=input("Digite el modo de pago : contado(C) o plazos(P) : ")
v=int(v)


if n == 'G' and p=='C':
    total=-v*(15/100)+v
    print("El total a pagar es : "  +str(total))

if n == 'G' and p=='P':
    total=-v*(10/100)+v
    print("El total a pagar es : "  +str(total))

if n == 'A' and p=='C':
    total=-v*(20/100)+v
    print("El total a pagar es : "  +str(total))

if n == 'A' and p=='P':
    total=-v*(5/100)+v
    print("El total a pagar es : "  +str(total))

    
    
   
