"""
For and while loops
"""


# my_list = ["1,2,3,4,5"]
# for data in my_list:
#     print(data)


# sum = 0
# for x in range(3,6):
#     sum += x
# print(sum)

# week_list = ["Monday", "Tuesday", "Wednesday", "Thursday"]
# for day in week_list:
#     print(f"Happy {day}!")


# While Loop

i = 0
# sum = 0
# while i < 5:
#     sum += i
#     i += 1
# print(sum)

while i < 5:
    i += 1
    if(i==3):
        continue
    print(i)
    if(i == 4):
        break
else:
    print("i is now larger or equal to 5")