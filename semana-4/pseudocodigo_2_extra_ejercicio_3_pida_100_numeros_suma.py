"""
Cree un diagrama de flujo que le pida 100 números 
al usuario y muestre la suma de todos.
"""

print("Digite 100 números")
suma_numero = 0

for i in range(5):
    numero_usuario= int(input("Digite un número: "))
    if numero_usuario > 0:
        suma_numero = suma_numero + numero_usuario
    else:
        print("Trate de nuevo. Digite un número positivo!")

print(f"La suma de todos los 100 número es:{suma_numero}")