# No. 1
filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()

print(contents)

# No. 2
print('')
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

# No. 3
print('')
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())