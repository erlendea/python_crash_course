import json

favorite_number = input("What is your favorite number? ")

filename = 'favorite_number.json'

with open(filename, 'w') as f:
    json.dump(favorite_number, f)
    print(f"Your favorite number, i.e. {favorite_number} has been written to the file {filename}.")


with open(filename) as f:
    number_read = json.load(f)
    print(f"I know your favorite number. It's {number_read}")