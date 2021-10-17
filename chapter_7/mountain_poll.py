responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the reponse in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person reponse (yes/no) ")

    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.

print(responses)
print('\n--- Poll results ---')
for name, reponse in responses.items():
    print(f"{name} would like to climb {reponse}.")