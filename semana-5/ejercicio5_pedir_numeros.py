lista_numeros = []

for i in range(10):
    numero = int(input("Ingrese el número: "))
    i=i+1
    lista_numeros.append(numero)

print(f"Los números ingresados son: {lista_numeros}")
print(f"El número más alto es: {max(lista_numeros)}")
