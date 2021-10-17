prompt = "Please enter pizza toppings:"
prompt += "\nEnter 'quit' when finished."

print(prompt)

while True:
    message = input('Add topping: ')

    if message == 'quit':
        break