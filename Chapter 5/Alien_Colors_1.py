# Chapter 5/Alien_Colors_1.py

import random
x = random.randint(1,3)
if x == 1:
    alien_color = "green"
elif x == 2:
    alien_color = "yellow"
else:
    alien_color = "red"
    
print(alien_color)

if alien_color == "green":
    print("You have just earned 5 points")
    
    