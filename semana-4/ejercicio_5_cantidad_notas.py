"""
5. Dada `n` cantidad de notas de un estudiante, calcular:
    1. Cuantas notas tiene aprobadas (mayor a 70).
    2. Cuantas notas tiene desaprobadas (menor a 70).
    3. El promedio de todas.
    4. El promedio de las aprobadas.
    5. El promedio de las desaprobadas.
"""

comprobar = True

while comprobar == True:
    cantidad_notas = int(input("Digite la cantidad de notas que quiere calcular: "))
    suma_notas = 0 
    if cantidad_notas > 0:
        
        comprobar = False

        promedio_notas_aprobadas = 0
        promedio_notas_desaprobadas = 0
        cantidad_notas_aprobadas = 0
        cantidad_notas_desaprobadas = 0
        suma_notas_aprobadas = 0
        suma_notas_desaprobadas = 0
        
        
        for i in range(cantidad_notas):
            nota = int (input("Ingrese una nota: "))
            suma_notas += nota
                
            if nota >= 70:
                cantidad_notas_aprobadas += 1
                suma_notas_aprobadas= suma_notas_aprobadas + nota
                promedio_notas_aprobadas = suma_notas_aprobadas / cantidad_notas_aprobadas
            else:
                cantidad_notas_desaprobadas += 1
                suma_notas_desaprobadas= suma_notas_desaprobadas + nota
                promedio_notas_desaprobadas = suma_notas_desaprobadas / cantidad_notas_desaprobadas
                
        promedio_total_notas = suma_notas /cantidad_notas

        print("\nCon los datos obtenidos se tiene que:"
            f"\nLa cantidad de notas aprobadas es: {cantidad_notas_aprobadas}"
            f"\nLa cantidad de notas desaprobadas es: {cantidad_notas_desaprobadas}"
            f"\nEl promedio de todas las notas aprobadas es: {promedio_notas_aprobadas:.2f}"
            f"\nEl promedio de todas las notas desaprobadas es: {promedio_notas_desaprobadas:.2f}"
            f"\nEl promedio de todas las notas es: {promedio_total_notas:.2f}")  
    else:
        print("Intente nuevamente. Digite una cantidad positiva! ")