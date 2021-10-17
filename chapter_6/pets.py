pet_1 = {
    'name': 'doogy dog',
    'animal type': 'dog',
    'owner': 'andrew bekkelund',
    }

pet_2 = {
    'name': 'rudolf',
    'animal type': 'reindeer',
    'owner': 'arne rykhus',
    }

pet_3 = {
    'name': 'bjørn',
    'animal type': 'bear',
    'owner': 'erlend aasheim',
    }

pets = [pet_1, pet_2, pet_3]

no = 1

for pet in pets:
    print(f"\nPet no. {no}:")
    no = no + 1

    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")
