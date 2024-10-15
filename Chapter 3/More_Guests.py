# Chapter 3/More_Guests.py
guest_wish_list = ["winnie", "betty", "matilda", "susanna"]
for x in guest_wish_list:
    print(f"Dear {x.title()}, I wish to invite you to dinner.")
print("We have a bigger table.")


# add a new guest to the beginning of the list.
guest_wish_list.insert(0,"judy")
# add another one to the middle of the list.
guest_wish_list.insert(2,"cecilia")
# add another to the end of the list.
guest_wish_list.append("maggie")

for x in guest_wish_list:
    print(f"Dear {x.title()}, I wish to invite you to dinner.")
    
print(guest_wish_list)