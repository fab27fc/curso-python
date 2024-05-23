"""
1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
"""
# 1. string + string → ?
nombre_1 = "Carlos"
apellido = "Marin"
print("La suma de string + string es: " + nombre_1 + apellido)

# 2. string + int → ?
palabra_anos = "años"
edad_1 = str(50)
print("La suma de string + int es: " + palabra_anos + edad_1)

# 3. int + string → ?
edad_2 = str(90)
palabra_anos = "años"
print("La suma de int + string es: " + edad_2 + palabra_anos)

# 4. list + list → ?
lista_1 = ["Fabian", "Carlos"]
lista_2 = ["Jose", "Ricardo"]
print("La suma de list + list es: " + str(lista_1 + lista_2))

# 5. string + list → ?
nombre_3 = "Jose"
lista_3 = ["Mario" , "Francisco"]
print("La suma de string + list es: " + str([nombre_3] + lista_3))

# 6. float + int → ?
numero_decimal = 38484749.90
numero_entero = 289
print("La suma de float + int es: " + str(numero_decimal + numero_entero))

# 7. bool + bool → ?
cierto = True
falso = False
print("La suma de bool + bool es: " + cierto + falso)