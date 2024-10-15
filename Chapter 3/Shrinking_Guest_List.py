# Chapter 3/Shrinking_Guest_List.py
guest_wish_list = ['judy', 'winnie', 'cecilia', 'betty', 'matilda', 'susanna', 'maggie']
for x in guest_wish_list:
	print(f"Dear {x.title()}, I am sorry I can only invite two to come to dinner.")
y = len(guest_wish_list)
print(y)
while y > 2:
	from random import randint
	z = randint(1, y)
	print(z) # for checking
	w = z -1 
	r = guest_wish_list.pop(w)
	print(r) # for checking
	print(f"Dear {r.title()}, I am sorry that there is a sudden change in space. I can only invite two to come to dinner. I cannot have a place for you.")
	y = len(guest_wish_list)
else:
    print(guest_wish_list) # for checking
for guest in guest_wish_list:
    print(f"Dear {guest.title()}, I am sorry that there is a sudden change in space. I can only invite two to come to dinner. You are still invited")
del guest_wish_list[0]
print(guest_wish_list)
del guest_wish_list[0]
print(guest_wish_list)