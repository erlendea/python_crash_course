filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as file_object:
        content = file_object.read()
except FileNotFoundError:
    print("The file you try to read, is not available.")
else:
    words = content.split()
    print(f"The file {filename} contains approximately {len(words)} of words.")