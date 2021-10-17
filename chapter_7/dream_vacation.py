dream_place = {}

while True:
    name = input('What is your name? ')
    place = input('If you could visit one place in the world, where would you go? ')

    dream_place[name] = place

    new_user = input('Would you like to add another user (yes/no): ')

    if new_user == 'no':
        break

print(dream_place)

for name, place in dream_place.items():
    print(f"{name} would like to go to {place}.")