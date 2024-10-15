rivers = {
    'jordan river': 'lebanon',
    'nile': 'ethipoia',
    'ganges': 'bangladesh',
    'yellow river': 'china',
    'yangtze river': 'china',
}

# This "dictionary" has 5 set of items (in this case, it is paired-items). The first component of the item is called key. The second component is the value of the key. The second component can be called by reference to the key. The second component can also be obtained by direct reference to the value.

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():   # note it is keys, not key
    print(f"- {river.title()}")
    

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")