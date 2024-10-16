# Chapter 7/Restaurant_Seating.py

prompt = "How many people are there in your dinner group? "
seats = input(prompt)
party_size = int(seats)
if party_size > 8:
    print("Please wait for a table.")
else:
    print("A table is ready.")