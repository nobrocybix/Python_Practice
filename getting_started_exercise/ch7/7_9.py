vancation_locations = []

while True:
    vancation_location = input("If you could visit one place in the world, where would you go? ")

    if vancation_location == 'quit':
        break
    
    vancation_locations.append(vancation_location)

print(vancation_locations)
