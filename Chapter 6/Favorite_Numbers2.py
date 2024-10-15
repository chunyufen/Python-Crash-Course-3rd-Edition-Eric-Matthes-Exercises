# Chapter 6/Favorite_Numbers2.py

favorite_numbers = {
    'john doe': [42, 17],
    'jane doe': [11, 39, 56],
    'john roe': [6, 12],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))