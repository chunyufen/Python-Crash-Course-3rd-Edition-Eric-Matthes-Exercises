# Chapter 3/Changing_Guest_List.py

guest_wish_list = ["flora", "betty", "matilda", "susanna"]
x = guest_wish_list[0].title()
print(f"{x} cannot come to the dinner.")
guest_wish_list[0] = "winnie"
for x in guest_wish_list:
    print(f"Dear {x.title()}, I wish to invite you to dinner.")
