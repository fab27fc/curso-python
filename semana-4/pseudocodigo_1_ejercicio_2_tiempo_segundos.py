"""
Cree un pseudocódigo que le pida un `tiempo en segundos` al usuario y calcule si es 
menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar 
a 10 minutos. Si es mayor, muestre “*Mayor*”.
    1. *Ejemplos*:
        1. 1040 → Mayor
        2. 140 → 460
        3. 599 → 1
"""

tiempo_segundos = int(input("Digite el tiempo en segundos: "))

segundos_faltantes = 0

if tiempo_segundos < 600:

    segundos_faltantes =  600 - tiempo_segundos 
    print(f"Los segundos que hacen falta para llegar a 10 minutos son: {segundos_faltantes} ")
else:
    print("El tiempo ingresado es:“*Mayor*” ")