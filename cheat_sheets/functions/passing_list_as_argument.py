def greet_users(names):
    """Print a simple greeting to everyone."""
    for name in names:
        msg = f"Hello, {name}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)