my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)

for numero in my_list[:]:
    if numero % 2 != 0:
        my_list.remove(numero) 

print(my_list)