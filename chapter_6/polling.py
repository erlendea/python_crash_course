favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

names_poll = ['sarah', 'phil']

for person in sorted(favorite_languages.keys()):
    if person in names_poll:
        print(f"{person.title()}, thanks for responding!")
    else:
        print(f"{person.title()}, please take the poll!")