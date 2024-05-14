"""
Cree un programa que le pida tres números al usuario 
y muestre el mayor.
"""
numeros =[]
print("Por favor digite 3 numeros:")

for i in range (3):    
    numero = int(input(f"Digite el número # {i+1}: "))
    numeros.append(numero)

mayor = numeros [0]

for numero in numeros:
    if numero > mayor:
        mayor = numero
print(f" El numero mayor es: {mayor}")
    



