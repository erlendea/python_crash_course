def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

user_names = ['ingrid', 'erlend', 'bjørn egil', 'beathe']
greet_users(user_names)