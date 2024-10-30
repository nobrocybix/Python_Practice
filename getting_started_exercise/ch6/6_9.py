favorite_places = {
    'winnie': ['taipei', 'new york', 'los angeles'],
    'chen': ['kowloon', 'japan', 'shanghai'],
    'chris': ['roma', 'italy', 'france'],
    'yoyo': ['amsterdam', 'berlin', 'chicago'],
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())