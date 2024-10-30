names = {
    'first_name': 'winnie',
    'last_name': 'Chen',
    'age': 18,
    'city': 'Taipei'
}

names_2 = {
    'first_name': 'Ryan',
    'last_name': 'Thomas',
    'age': 60,
    'city': 'England'
}

names_3 = {
    'first_name': 'Tom',
    'last_name': 'Clark',
    'age': 28,
    'city': 'New York'
}

names_list = [names, names_2, names_3]

for name in names_list:

    print(name['first_name'])
    print(name['last_name'])
    print(name['age'])
    print(name['city'])

    print("\n")