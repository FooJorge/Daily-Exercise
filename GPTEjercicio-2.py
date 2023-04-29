# Ejercicio: Escribe un programa que solicite al usuario un número y luego muestre 
# la tabla de multiplicar correspondiente a ese número.

num = int(input("Introduce un número entero: "))

for i in range(1, 11):
    resultado = num * i
    print("{} x {} = {}".format(num, i, resultado))

