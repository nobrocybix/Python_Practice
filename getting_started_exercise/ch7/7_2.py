group = input("How many people are in your dinner group? " )

group = int(group)
if group > 8:
    print("You have to wait for a table.")
else:
    print("You have " + str(group) + " people in your dinner group.")