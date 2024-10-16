# Chapter 7/Movie_Tickets.py

prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("\tYou get in free!")
    elif age < 13:
        print("\tYour ticket is $10.")
    else:
        print("\tYour ticket is $15.")