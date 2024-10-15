# Chapter 5/Ordinal_Numbers.py

numbers_list = [] # make an empty list to start storing
numbers_list = list(range(1,10))
print(numbers_list)

for number in numbers_list:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
