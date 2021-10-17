pizzas = ['grandiosa', 'big one', 'dr. oetker']
friend_pizzas = pizzas[:]

pizzas.append('arnes pizza')
friend_pizzas.append('andrews pizza')

print(pizzas)
print(friend_pizzas)

print("\nMy favorite pizzas are:")

for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")

for friend_pizza in friend_pizzas:
    print(friend_pizza.title())