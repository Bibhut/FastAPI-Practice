"""
Dictionaries
"""


user_dictionary = {
    'username' : 'code with bibhut',
    'name': 'Bibhut',
    'age': 35
}


# print(user_dictionary.get("username"))
# user_dictionary["married"] = True
# print(user_dictionary)
# print(len(user_dictionary))
# user_dictionary.pop('age')
# print(user_dictionary)


# Need to use copy if not it treats as the same variable
# all changes will be also removed in main variable as well if copy is not used. 
user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop('age')
print(user_dictionary)
print(user_dictionary2)
