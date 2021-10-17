print("Ticket prices")
print("If you want to quit, type 'quit'")

age = ' '

while age != 'quit':
    age = input("Give your age (quit? -> 'quit'): ")
    
    if age != 'quit':
        age = int(age)

        if age < 3:
            print("The ticket is free :-)")
        elif age < 12:
            print("The ticket costs $10")
        elif age >=12:
            print("The ticket costs $15")