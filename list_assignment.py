"""
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals
"""


zoo = ["Monkey", "Rhino", "Elephant", "Deer", "Tiger"]
zoo.pop(3)
zoo.append("Kangaroo")
zoo.pop(0)

for i in zoo:
    print(i)
print(zoo[0:3])
