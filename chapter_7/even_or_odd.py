number = input("Enter a number, and I will tell you if it is even or odd: ")
number = int(number)

test = number%2

if test == 0:
    print(f"The number you have written, i.e. {number} is even.")
elif test != 0:
    print(f"The number you have written, i.e. {number} is odd.")

