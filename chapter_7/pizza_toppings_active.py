prompt = "Please enter pizza toppings:"
prompt += "\nEnter 'quit' when finished."

print(prompt)

active = True

while active:
    message = input('Add topping: ')

    if message == 'quit':
        active = False