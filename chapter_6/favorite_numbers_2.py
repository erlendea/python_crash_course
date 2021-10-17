favorite_numbers = {
    'arne': [10, 20],
    'andrew': [6, 15, 30, 90],
    'erlend': [8],
    'ingrid': [75, 29090],
    'gunn': [2585, 300, 4400, 500],
}

i = 1

for person, numbers in favorite_numbers.items():
    print(f"\nPerson no. {i}; {person.title()}'s favorite numbers:")
    i = i + 1
    
    for number in numbers:
        print(f"\t{number}")