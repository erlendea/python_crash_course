prompt = "Please enter pizza toppings:"
prompt += "\nEnter 'quit' when finished."

print(prompt)

message = " "

while message != 'quit':
    message = input('Add topping: ')

    if message != 'quit':
        print(message)