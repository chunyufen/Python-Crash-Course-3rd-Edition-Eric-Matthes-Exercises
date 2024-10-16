# Chapter 7/Dream_Vacation.py

name_prompt = "\nWhat is your name? "
place_prompt = "\nIf you could visit any place in the world, where would it be? "
next_prompt = "\nWould you like to let someone else answer? (yes/no) "

vacations = {} # {name: place}

while True:
    name = input(name_prompt)
    place = input(place_prompt)
    vacations[name] = place
    next = input(next_prompt)
    if next != 'yes':
        break

print("\n----- Results -----")
for name, place in vacations.items():
    print(f"{name.title()} would like to go to {place.title()}.")
    