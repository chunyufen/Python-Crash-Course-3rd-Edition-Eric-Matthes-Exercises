# Chapter 4/My_Pizzas_Your_Pizzas.py

pizzas = ['Cheese Pizza', 'Veggie Pizza', 'Pepperoni Pizza']

print("This is my orginal pizzas list:")
for pizza in pizzas:
    print(f"{pizza}")

friend_pizzas = pizzas[:]

print("\nThis is my friend's pizzas list:")
for friend_pizza in friend_pizzas:
    print(f"{friend_pizza}")

print("\nThis is my new pizza list:")
pizzas.append('Hawaiian Pizza')
for pizza in pizzas:
    print(f"{pizza}")

print("\nThis is my friend's new pizza list:")
friend_pizzas.append('Greek Pizza')
for pizza in friend_pizzas:
    print(f"{pizza}")
