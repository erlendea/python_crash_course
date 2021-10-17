number = input('Please enter a number: ')
number = int(number)

test = number%10

if test == 0:
    print(f"You're number, i.e. {number}, is a multiple of 10")
else:
    print(f"You're number, i.e. {number}, is not a multiple of 10")
