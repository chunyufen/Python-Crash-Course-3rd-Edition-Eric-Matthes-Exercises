# Chapter 9/Dice.py

from random import randint # random integer

# create a model for die and throw

class Die:
    def __init__(self, sides=6):
        # sides = 6
        self.sides = sides
    
    def roll_die(self): # meaning getting a random number
        return randint(1, self.sides)

# 6-sided die thrown 10 times

die_6 = Die() # default is 6

results = []
for roll_num in range(10):
    result = die_6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
for result in results:
    print(result)
    
# 10-sided die thrown 10 times

die_10 = Die(10) # need to say 10, not default

results = []
for roll_num in range(10):
    result = die_10.roll_die()
    results.append(result)
print("10 rolls of a 10-sided die:")
for result in results:
    print(result)
    
# 20-sided die thrown 10 times

die_20 = Die(20) # need to say 20, not default

results = []
for roll_num in range(10):
    result = die_20.roll_die()
    results.append(result)
print("10 rolls of a 20-sided die:")
for result in results:
    print(result)
  