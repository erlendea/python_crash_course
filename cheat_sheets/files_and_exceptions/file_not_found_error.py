#f_name = 'siddhartha.txt'

f_name = 'siddhartha_TEST#.txt'

try:
    with open(f_name) as f:
        lines = f.readlines()
except FileNotFoundError:
    msg = f"Can’t find file: {f_name}."
    print(msg)