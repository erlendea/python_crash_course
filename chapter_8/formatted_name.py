def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name.lower()} {middle_name.lower()} {last_name.lower()}"
    else:
        full_name = f"{first_name.lower()} {last_name.lower()}"
    return full_name.title()

musician = get_formatted_name('jIMI', 'hEnDrIx', 'Erlend')
print(musician)


print('')
musician = get_formatted_name(middle_name='Erlend', first_name='jIMI', last_name='hEnDrIx',)
print(musician)