favorite_places = {
    'andrew': ['norge', 'sverige', 'danmark'],
    'erlend': ['norge', 'kroatia', 'australia'],
    'arne': ['norge', 'vinstra', 'vidda'],
}

i = 1

for person, places in favorite_places.items():
    print(f"\nPerson no. {i}; {person.title()}'s favorite places:")
    i = i + 1
    
    for place in places:
        print(f"\t{place.title()}")