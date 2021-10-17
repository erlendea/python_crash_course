import json
f_name = 'numbers.json'

try:
    with open(f_name) as f:
        numbers = json.load(f)
except FileNotFoundError:
    msg = f"Can’t find file: {f_name}."
    print(msg)
else:
    print(numbers)