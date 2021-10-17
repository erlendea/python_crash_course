sandwich_orders = ['turkey sandwich', 'ham sandwich', 'veggie sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"I made your {current_sandwich}!")

    finished_sandwiches.append(current_sandwich)

print(f"\nThe following sandwiches have been made:")

for finished_sandwich in finished_sandwiches:
    print(f"\t{finished_sandwich}")

print(" ")
print(sandwich_orders)
print(finished_sandwiches)