employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}
list_of_keys = ['access_level', 'age']

for key in list_of_keys:
    if key in employee:
        del employee[key]
        
print(employee)
