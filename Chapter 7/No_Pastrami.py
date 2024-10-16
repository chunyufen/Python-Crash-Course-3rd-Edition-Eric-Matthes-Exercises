# Chapter 7/No_Pastrami.py

sandwich_orders = ['pastrami', 'chicken', 'seafood', 'pastrami', 'roast beef', 'grilled cheese', 'ham', 'pastrami']
print("I am worry, we do not have pastrami sandwich today.")

no_supply = 'pastrami'

while no_supply in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []
while sandwich_orders:
    sandwich_made = sandwich_orders.pop()
    print(f"I am preparing your {sandwich_made} sandwich.")
    finished_sandwiches.append(sandwich_made)
print("\n")
for sandwich in finished_sandwiches:
    print(f"I have made a {sandwich} sandwich.")