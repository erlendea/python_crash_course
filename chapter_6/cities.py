cities = {
    'oslo': {
        'country': 'norway',
        'population': 700_000,
        'fact': 'This is the capitol of Norway',
    },

    'split': {
        'country': 'crotia',
        'population': 200_000,
        'fact': 'This is a large city in Croatia',
    },

    'røros': {
        'country': 'norway',
        'population': 5_000,
        'fact': 'This is a small city in the middle of Norway',
        'fun-fact': 'Erlend is born here',
    },
}


for city, facts in cities.items():
    print(f"{city.title()} facts:")

    for fact, data in facts.items():
        print(f"\t{fact.title()}: {data}")