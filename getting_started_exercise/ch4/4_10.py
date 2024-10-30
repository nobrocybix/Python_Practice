pizzas = ['Veggie', 'Margherita,', 'Pepperoni', 'Hawaiian']

friend_pizzas = pizzas[:]
pizzas.append('cheese')
friend_pizzas.append('mushroom')

for pizza in pizzas:
    print("My favorite pizzas are:" + pizza)

for friend_pizza in friend_pizzas:
    print("My friend's favorite pizzas are:" + friend_pizza)