# Ejercicio: Escribe un programa que solicite al usuario un número y luego muestre 
# la tabla de multiplicar correspondiente a ese número.

a=input('Introduce un número de 1 al 10: ')
b=int(a)
for i in range(1,11):
    print(i,'x',b,'=',i*b)
