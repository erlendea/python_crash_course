# No. 1
filename = 'learning_python.txt'

print('')
with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    line_mod = line.replace('Python', 'C')
    print(line_mod.strip())