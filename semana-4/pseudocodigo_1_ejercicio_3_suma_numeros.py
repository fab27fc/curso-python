"""
Cree un algoritmo que le pida un numero al usuario y muestre la suma de todos los números desde 1 hasta ese número.
    1. 3 → 6 (1 + 2 + 3)
    2. 5 → 15 (1 + 2 + 3 + 4 + 5) 
    3. 12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)
"""
numero_usuario = int(input("Ingrese un numero: "))
sumar_contador = 0

if numero_usuario > 0:

    for i in range(1,numero_usuario +1):
       sumar_contador = sumar_contador + i


print(f"La suma de todos dos los números es: {sumar_contador}")