"""
2. Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s. Recuerda que `1 km == 1000m` y `1 hora == 60 segundos`.
    1. *Ejemplos*:
        1. 73 → 20.27
        2. 50 → 13.88
        3. 120 → 33.33
"""
velocidad_km = int(input("Ingrese una velocidad en Kilometros: "))

conversion_metros= 0

if velocidad_km > 0:
    conversion_metros = velocidad_km * 1000
    print(f"La conversión de {velocidad_km} km a metros es: {conversion_metros} metros ")
