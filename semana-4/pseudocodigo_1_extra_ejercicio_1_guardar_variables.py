"""
Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas 
(`primero` y `segundo`) y los ordene de menor a mayor en dichas variables.
    a. Ejemplos:
        1. A: 56, B: 32 → A: 32, B: 56
        2. A: 24, B: 76 → A: 24, B: 76
        3. A: 45, B: 12 → A: 12, B: 45
"""
primero = int(input("Ingrese el primer número: "))
segundo = int(input("Ingrese el segundo número: "))

print("\nLos números se ordenaran de menor a mayor:",end="")

if primero > segundo:
    print(f"\nPrimero: {segundo}",
          f"\nSegundo: {primero}")
else:
    print(f"\nPrimero: {primero}",
          f"\nSegundo: {segundo}")