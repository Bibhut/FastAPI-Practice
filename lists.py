
"""
List is just a collection of data
"""

my_list = [80,98,232,2323,"erwerw"]

print(my_list)

# To print last element of the list
print(my_list[-1])

# Update the list
my_list[1] = "Hello"

print(my_list)

# get length of the list
print(len(my_list))

# Slicing the list
#Starts from 0 index and ends and 2 index
print(my_list[0:2])

#Insert and delete

my_list.append(1000)
print(my_list)

my_list.insert(2,1000)
print(my_list)

my_list.remove("erwerw")
print(my_list)

my_list.pop(1)
print(my_list)

my_list.sort()
print(my_list)