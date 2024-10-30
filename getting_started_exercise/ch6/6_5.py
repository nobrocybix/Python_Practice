country ={'nile': 'egypt', 'yellow river': 'china', 'amazon river': 'brazil'}

for river, nation in country.items():
    print("The " + river.title() + " runs through " + nation.title() + ".")

for river in country.keys():
    print(river.title())

for country in country.values():
    print(country.title())  