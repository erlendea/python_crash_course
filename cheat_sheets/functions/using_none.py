def describe_pet(animal, name=None):
    """Display information about a pet."""
    print(f"\nI have a {animal}.")
    if name:
        print(f"Its name is {name}.")
describe_pet('hamster', 'harry')
describe_pet('snake')