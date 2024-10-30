sandwich_orders = ['Chicken Sandwich', 'Beef Sandwich', 'Veggie Sandwich']

finished_sandwiches = []

for sandwich in sandwich_orders:
    print("I made your " + sandwich.lower() + ".")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)