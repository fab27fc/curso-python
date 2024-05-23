my_favorite_records = [
    "Dark Side Of the Moon",
    "Fear of a Blank Planet",
    "Signify",
    "Fabian",
]

for record in my_favorite_records:
    if record == "Signify":
        print("Hey, este es mi signify!")
    else:
        print(f"Record: {record}")

for index in range(0,len(my_favorite_records)):
    record = my_favorite_records[index]
    print(f"Record {index}: {record}")

for index in range(0, 15):
    print(index)

index = 0
while index < len(my_favorite_records):
    record = my_favorite_records[index]
    print(f"Record {index}:   {record}")
    index += 1


for index, record in enumerate(my_favorite_records):
    print(f"Record {index}:-> {record}")

my_string = "Hola mundo"

print(my_string[0])

for character in my_string:
    print(character)

colors = [
    "black",
    "yellow",
    "red",
    "blue",
]

for color in colors:
    print(color)
    if color== "red":
        break

counter = 0
while True:
    print("INFINIDAD")
    if counter > 3:
        break
    counter += 1








