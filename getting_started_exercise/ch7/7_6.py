active = True

while active:
    ages = input("Enter you age: ")

    if ages == 'quit':
        active = False
    elif int(ages) < 3:
        print("The ticket price is free.")
    elif int(ages) >= 3 and int(ages) <= 12:
        print("The ticket price is $10.")
    elif int(ages) > 12:
        print("The ticket price is $15.")