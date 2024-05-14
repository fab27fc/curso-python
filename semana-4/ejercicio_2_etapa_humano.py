"""
Cree un programa que le pida al usuario su nombre, apellido, 
y edad, y muestre si es un bebé, niño, preadolescente, 
adolescente, adulto joven, adulto, o adulto mayor.
"""

nombre = input("Digite su nombre: ")
apellido = input("Digite su apellido: ")
edad = int (input("Digite su edad: "))


if edad > 0 and edad < 2:
    print(f"La persona con el nombre: {nombre} con el apellido {apellido} es un bebé.")
elif edad >= 3 and edad <= 10:
    print(f"La persona con el nombre: {nombre} con el apellido {apellido} es un niño.")
elif edad >= 10 and edad <= 12:
    print(f"La persona con el nombre: {nombre} con el apellido {apellido} es un preadolescente.")
elif edad >= 13 and edad <= 19:
    print(f"La persona con el nombre: {nombre} con el apellido {apellido} es un adolescente.")
elif edad >= 20 and edad <= 39:
    print(f"La persona con el nombre: {nombre} con el apellido {apellido} es un adulto joven.")
elif edad >= 40 and edad <= 64:
    print(f"La persona con el nombre: {nombre} con el apellido {apellido} es un adulto.")
else:
    print(f"La persona con el nombre: {nombre} con el apellido {apellido} es un adulto mayor.")
