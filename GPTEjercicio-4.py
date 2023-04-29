# Ejercicio: Escribe un programa que solicite al usuario una palabra y luego muestre
# la palabra invertida.

palabra=input('Dime una palabra: ')
# palabra_invertida=palabra[:1] Esto me devolvería la primera letra de la palabra
#palabra_invertida=palabra[:2] Esto devuelve las dos primeras letras de la palabra
#palabra_invertida=palabra[::3] Entiendo que cuando hay ::n implica que da saltos cana n
                                #En este caso sería "po"
palabra_invertida=palabra[::-1] #Aquí da saltos de -1 en -1. Por lo que da la vuelta a la palabra
print("La palabra invertida es:",palabra_invertida)