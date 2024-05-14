"""
Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor.
    1. *Ejemplos*:
        1. 4, 76, 43, 6, 8 → 76
        2. 1, 2, 3, 6, 7 → 7
        3. 2132, 4355, 1132, 2323, 1214 → 4355
"""
print("Digite 5 números")
numero_mayor = 0
for i in range(5):
    numero_usuario= int(input("Digite un número: "))
    if numero_usuario > numero_mayor:
        numero_mayor = numero_usuario
print(f"El número mayor es: {numero_mayor}")