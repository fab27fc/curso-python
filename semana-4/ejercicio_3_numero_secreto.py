"""
Cree un programa con un numero secreto del 1 al 10. El 
programa no debe cerrarse hasta que el usuario adivine 
el numero.
"""

import random
numero_secreto = random.randint(1,10)

while True:
    numero_usuario = int(input("Digite un número del 1 al 10 para adivinar el número secreto: "))

    if numero_usuario != numero_secreto:
        print("Número secreto no adivinado, intente de nuevo!")
        
    else:
        print(f"Número secreto fue acertado!\n El número secreto es: {numero_usuario}")
        break

