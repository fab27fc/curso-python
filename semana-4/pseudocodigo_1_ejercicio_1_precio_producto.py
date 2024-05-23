"""
1. Cree un pseudocódigo que le pida un `precio de producto` al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
    1. Si el precio es menor a 100, el descuento es del 2%.
    2. Si el precio es mayor o igual a 100, el descuento es del 10%.
    3. *Ejemplos*:
        1. 120 → 108
        2. 40 → 39.2
"""
precio_producto = int(input("Ingrese el precio de un producto: "))

precio_final_descuento = 0
calculo_descuento = 0

if precio_producto < 100:
    descuento_02 = 0.02
    
    calculo_descuento = precio_producto * descuento_02
    precio_final_descuento = precio_producto - calculo_descuento
    print("\nA este producto se le aplica un 2% de descuento." 
          f"\nTotal de descuento aplicado en el producto: {calculo_descuento}")
    

else:
    descuento_10 = 0.10
    calculo_descuento = precio_producto * descuento_10
    precio_final_descuento = precio_producto - calculo_descuento
    print("\nA este producto se le aplica un 10% de descuento." 
          f"\nTotal de descuento aplicado en el producto: {calculo_descuento}")

print(f"\nEl precio final del producto con el descuento es: {precio_final_descuento}"
        "\nGracias!")