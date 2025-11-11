days_left_for_birthday = int(input(" How many days until your birthday? "))
total_weeks = days_left_for_birthday/ 7


# To just delete decimal field use int
print(f"So you have approx {int(total_weeks)} weeks left for your birthday")


# For round about result use round method
print(f"So you have approx {round(total_weeks)} weeks left for your birthday")