Charlie = {'species': 'cat', 'name': 'Charlie', 'owner': 'Mark'}
Tom = {'species': 'dog', 'name': 'Tom', 'owner': 'Alex'}
Ryan = {'species': 'rabbit', 'name': 'Ryan', 'owner': 'Frank'}
winnie = {'species': 'guinea pig', 'name': 'Frank', 'owner': 'Kevin'}

pets = [Charlie, Tom, Ryan, winnie]

for pet in pets:
    print("I have a " + pet['species'] + " " + pet['name'] + " " + pet['owner'] + " " + "pets.")
