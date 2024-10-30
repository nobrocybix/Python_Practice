names = ['Ace', 'Brady', 'Charlie', 'Darcy', 'Elwin']
unable_names = names[0]
names[0] = 'Alex'
message = "and I have dinner together."

print(names[0] + " " + message)
print(names[1] + " " + message)
print(names[2] + " " + message)
print(names[3] + " " + message)
print(names[4] + " " + message) 

print(unable_names + " " + "can't come")