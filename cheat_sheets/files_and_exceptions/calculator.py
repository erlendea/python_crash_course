"""A simple calculator for division only."""
print("Enter two numbers. I'll divide them.")
print("Enter 'q' to quit.")
while True:
    x = input("\nFirst number: ")
    if x == 'q':
        break
    y = input("Second number: ")
    if y == 'q':
        break
    try:
        result = int(x) / int(y)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(result)