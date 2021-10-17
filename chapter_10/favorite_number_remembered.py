import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        number_read = json.load(f)       
except FileNotFoundError:
    with open(filename, 'w') as f:
        favorite_number = input("What is your favorite number? ")
        json.dump(favorite_number, f)
        print(f"Your favorite number, i.e. {favorite_number} has been written to the file {filename}.")
else:
     print(f"I know your favorite number. It's {number_read}")