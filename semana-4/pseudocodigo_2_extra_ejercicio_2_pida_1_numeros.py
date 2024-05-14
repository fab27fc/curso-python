"""
Cree un diagrama de flujo que le pida un numero al usuario y muestre “*Fizz*” si es divisible entre 3, 
“*Buzz*” si es divisible entre 5, y “*FizzBuzz*” si es divisible entre ambos.
    1. *Ejemplos*:
        1. 33 → Fizz
        2. 25 → Buzz
        3. 30 → FizzBuzz
"""

numero_usuario= int(input("Digite un número: "))

if numero_usuario % 5 == 0 and numero_usuario % 3==0:
    print("*FizzBuzz*")
elif numero_usuario % 5 == 0:
    print("*Buzz*")
else:
    numero_usuario % 3 ==0
    print("*Fizz*")