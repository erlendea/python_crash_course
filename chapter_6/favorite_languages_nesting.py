favorite_languages = {
    'jen':  ['python', 'ruby','c'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name in favorite_languages.keys():
    if len(favorite_languages[name]) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
    else:
        print(f"\n{name.title()}'s favorite language is:")

    
    i = 1

    for language in favorite_languages[name]:        
        print(f"\tNo. {i}: {language.title()}")
        i = i + 1