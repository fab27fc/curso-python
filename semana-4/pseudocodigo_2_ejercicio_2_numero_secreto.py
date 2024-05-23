"""
Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, y le 
pida al usuario adivinar ese número. El algoritmo no debe terminar 
hasta que el usuario adivine el numero.
"""
import random

while True:
    numero_secreto = random.randint(1,10)
    numero_usuario = int(input("Ingrese un número: "))

    if numero_secreto == numero_usuario:
        print(f"El número secreto es: {numero_usuario}")
        break
    else:
        print("Intente de nuevo. Digite otro número: ")