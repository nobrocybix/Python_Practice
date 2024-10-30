cities = {
    'New York' : {
        'country': 'America',
        'population': 8.5,
        'fact': 'New York is the most populous city in the United States.',
    }, 

    'Los Angeles' : {
        'country': 'America',
        'population': 3.7,
        'fact': 'Los Angeles is the second-most populous city in the United States.',
    },

    'Shanghai' : {
        'country': 'China',
        'population': 24.5,
        'fact': 'Shanghai is the most populous city in China.',
    }, 

    'Taipei' : {
        'country': 'Taiwan',
        'population': 3.5,
        'fact': 'Taipei is the most populous city in Taiwan.',  
    },
}


for city, info in cities.items():
    print("\nCity: " + city)
    print("Country: " + info['country'])
    print("Population: " + str(info['population']))
    print("Fact: " + info['fact'])