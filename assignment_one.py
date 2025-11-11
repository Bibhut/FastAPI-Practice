
"""
Write a Python program that can do the following:

- You have $50

- You buy an item that is $15, that has a 3% tax

- Using the print()  Print how much money you have left, after purchasing the item.

"""

amount_i_have = 50
item_price = 15
tax = 3
total_item_price = item_price + (item_price * tax/100)
print(total_item_price)

left_amount = amount_i_have - total_item_price
print(left_amount)