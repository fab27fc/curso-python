"""
3. Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, 
mostrar “”. Sino, mostrar “*incorrecto*”.
    1. *Ejemplos*:
        1. 23, 30, 768 → Correcto (hay un 30)
        2. 10, 15, 5 → Correcto (10 + 15 + 5 = 30)
        3. 35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)
"""
lista =[]
print("Por favor ingrese 3 números: ")
suma_numeros = 0

for i in range(3):
    numero_usuario = int(input("Ingrese un numero: "))
    suma_numeros = suma_numeros + numero_usuario
    lista.append(numero_usuario)

if 30 in lista or suma_numeros == 30:
    print("*Correcto*")
else:
    print("*Incorrecto*")