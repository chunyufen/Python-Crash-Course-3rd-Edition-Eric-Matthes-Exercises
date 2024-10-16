# Chapter 7/Deli.py

sandwich_orders = ['chicken', 'seafood', 'roast beef', 'grilled cheese', 'ham']
finished_sandwiches = []
while sandwich_orders:
    sandwich_made = sandwich_orders.pop()
    print(f"I am preparing your {sandwich_made} sandwich.")
    finished_sandwiches.append(sandwich_made)
print("\n")
for sandwich in finished_sandwiches:
    print(f"I have made a {sandwich} sandwich.")


