# Chapter 9/Lottery_Analysis.py

import random

my_bet = ['a', '2', 'c', '4']
lottery = ('a', 'b', 'c', 'd', 'e',
           '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
result = random.choices(lottery, k = len(my_bet)) # this is the first draw
draw = 1

while result != my_bet:
    result = random.choices(lottery, k = len(my_bet)) # this is the second draw
    draw += 1

if draw == 1:
    print(f"It only took you {draw} try to win the lottery!")
else:
    print(f"It took you {draw} tries to win the lottery!")