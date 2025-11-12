"""
Sets are similar to lists but are unordered and cannot obtain duplications
Use curly brackets.
"""

my_set = {1,2,5,10,8,2,1}
print(my_set)

# Only counts unique elements
print(len(my_set))


my_set.discard(2)
print(my_set)

my_set.clear()
print(my_set)

my_set.add(2)
print(my_set)

my_set.update([7,8])
print(my_set)


"""
Tuples are just like lists but they are unchangeable
"""

my_tuples = (1,2,3,4,5,6)
print(my_tuples)
print(len(my_tuples))
print(my_tuples[1])

