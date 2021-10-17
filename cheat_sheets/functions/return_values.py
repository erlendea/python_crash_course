def get_full_name(first, last):
    """Return a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()
musician = get_full_name('jimi', 'hendrix')
print(musician)