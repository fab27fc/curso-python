"""
Cree un diagrama de flujo que le pida 100 números al usuario y muestre el mayor de todos.
    1. *Ejemplos*:
        1. 4, 76, 43, 6, 8 → 76
"""

print("Por favor ingrese 100 números: ")
lista=[]
for i in range(5):
    numero_usuario = int(input("Ingrese un número: "))
    lista.append(numero_usuario)
    mayor = max(lista)
print(f"El número mayor es: {mayor}")

