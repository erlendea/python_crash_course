print("Program for adding numbers")
print("Write 'q' at any time to exit")

while True:
    number_1 = input('Write a number: ') 
    
    if number_1 == 'q':
        break

    number_2 = input('Write a second number: ')

    if number_2 == 'q':
        break

    try:        
        sum_numbers = float(number_1) + float(number_2)
    except ValueError:
        print("You cannot write a string")
    else:
        print(f"The sum of the two numbers is {sum_numbers}\n")
