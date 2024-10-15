# Chapter 5/Stages_Of_Life.py

import random
age = [] # make an empty list first
age = random.randint(1,120)

if age < 2:
    group = "a baby"
elif 2 <= age < 4:
    group = "a toddler"
elif 4 <= age < 13:
    group = "a kid"  
elif 13 <= age < 20:
    group = "a teenager"   
elif 20 <= age < 65:
    group = "an adult"   
elif 65 <= age:
    group = "an elder"
print(f"You are {group}.")