print("El propósito de este programa es encontrar el valor del area debajo de la curva de la integral e^e^x en un intervalo (a,b) mediante el método del rectángulo")
a=float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))

while a > 6.5 or b > 6.5 :
    print("Los valores de la integral por encima de 6.5 son muy grandes para ser procesados. Por favor eliga un intervalo diferente.")
    a=float(input("Ingrese el valor de a: "))
    b=float(input("Ingrese el valor de b: "))
    
if a > b :
    c = b
    b = a
    a = c

n=int(input("Ingrese el número de rectángulos: "))
while n <= 0:
    print("El numero de rectángulos debe ser mayor a cero.")
    n=int(input("Ingrese el número de rectángulos: "))

e=2.71828

DX=((b-a)/n)
I=DX
SUMI=I+a
RESIZQ=0
RESDER=0
RESMED=0
RES=0
#cont=1


"""
while (SUMI<=b):
    RES=(DX*(e**e**(SUMI)))
    RESDER+=RES
    SUMI+=I
    print(cont)
    cont+=1
"""

for i in range (0, n, 1):
    RES=(DX*(e**e**(SUMI)))
    RESDER+=RES
    RESM=(DX*(e**e**(SUMI-(I/2))))
    RESMED += RESM
    SUMI+=I
    #print(cont)
    #cont+=1

    
RESIZQ = RESDER - RES
RES=(DX*(e**e**(a)))
RESIZQ += RES

print("El resultado se encuentra en el intervalo:")
print(RESDER)
print(RESIZQ)
print("El resultado se aproxima a: ", RESMED)
input()
