sandwich_orders = ['turkey sandwich', 'pastrami sandwich', 'ham sandwich', 'pastrami sandwich', 'veggie sandwich', 'pastrami sandwich']
finished_sandwiches = []

print("Deli has run out of pastrami")


while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

print(sandwich_orders)

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