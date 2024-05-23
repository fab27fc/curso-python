
my_list = [4, 3, 6, 1, 7]
print(my_list)
for i in range(len(my_list)):
    if i == 0:
        primero_lista = my_list[0]
    elif i == len(my_list) - 1:
        my_list[0], my_list[i] = my_list[i], primero_lista

print(my_list)


