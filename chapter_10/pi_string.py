filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string[:52])
print(len(pi_string))

birthday = '120372' 

if birthday in pi_string:
    print('Your birthday is in pi! :-)')
else:
    print('Your birthday is not in pi :-(')

# Converting pi_string from string to float
# number = float(pi_string) + 1
# print(number)