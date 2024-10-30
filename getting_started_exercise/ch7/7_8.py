sandwich_orders = ['Chicken Sandwich', 'Pastrami Sandwich',
                    'Beef Sandwich', 'Veggie Sandwich',
                    'Pastrami Sandwich', 'Pastrami Sandwich']

finished_sandwiches = []

for sandwich in sandwich_orders:
    print("I made your " + sandwich.lower() + ".")
    finished_sandwiches.append(sandwich)

    while 'Pastrami Sandwich' in finished_sandwiches:
        finished_sandwiches.remove('Pastrami Sandwich')

print(finished_sandwiches)