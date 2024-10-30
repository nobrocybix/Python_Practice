favourite_numbers = {
    'winnie': [7, 12, 54, 12],
    'chen': [8, 88, 23, 34],
    'chris': [34, 56, 77, 89],
    'yoyo': [2, 4, 6, 10, 33],
}

for name, numbers in favourite_numbers.items():
    print("My favourite numbers of " + name.title() + " are:")
    for number in numbers:
        print(str(number))
    print("\n")