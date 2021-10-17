person_1 = {
    'first_name': 'andrew',
    'last_name': 'bekkelund',
    'age': 47,
    'city': 'oslo',
    }

person_2 = {
    'first_name': 'arne',
    'last_name': 'rykhus',
    'age': 47,
    'city': 'vinstra',
    }

person_3 = {
    'first_name': 'erlend',
    'last_name': 'aasheim',
    'age': 47,
    'city': 'røros',
    }

people = [person_1, person_2, person_3]
print(people)

no = 1

for person in people:
    print(f"\nUser data, user no. {no}:")
    no = no + 1

    for key, value in person.items():
        print(f"{key}: {value}")
        print(f"{key}: {value}")