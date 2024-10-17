# Chapter 9/Lottery.py

from random import choice

pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# choice only pull 1 choice at 1 time, need to repeat

winning_lots = []
while len(winning_lots) < 4:
    pulled_lot = choice(pool)
    if pulled_lot not in winning_lots:
        print(f"One of the winning lot is {pulled_lot}.")
        winning_lots.append(pulled_lot)
print("The winning lots are:")
for winning_lot in winning_lots:
    print(winning_lot)
    

