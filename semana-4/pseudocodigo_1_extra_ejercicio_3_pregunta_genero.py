"""
3. Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, ingresando 1 si es mujer
o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.
1. *Ejemplos*:
        1. 1, 1, 1, 2, 2, 2 → 50% mujeres y 50% hombres
        2. 1, 1, 2, 2, 2, 2 → 33.3% mujeres y 66.6% hombres
        3. 1, 1, 1, 1, 1, 2 → 84.4% mujeres y 16.6% hombres
"""

print("Digite un número de acuerdo al sexo de 6 personas:"
      "\n1- Si es mujer"
      "\n2- Si es hombre")



porcentaje_hombres = 0
porcentaje_mujeres = 0
contador_hombres = 0
contador_mujeres = 0

for i in range (6):
    while True:
        try:
            numero = int(input("Digite el número: ")) 
        except:
            print("No es un número")
        #numero = int(input("Digite el número: "))  
        if numero == 1:
            contador_mujeres = contador_mujeres + 1
            porcentaje_mujeres = (contador_mujeres/6) * 100
            break   
        elif numero ==2: 
            contador_hombres = contador_hombres + 1
            porcentaje_hombres = (contador_hombres/6) * 100
            break
        else:        
            print("Digite 1 o 2 de acuerdo al sexo de la persona")
                
print(f"El porcentaje de mujeres es: {porcentaje_mujeres}"
      f"\nEl porcentaje de hombres es: {porcentaje_hombres}")


    

