# Chapter 7/Multiples_Of_Ten.py

prompt = "Give me a number: "
reply = input(prompt)
number = int(reply)
if number % 10 == 0:
    print("This number is a multiple of 10.")
else:
    print("This number is not divisible by 10.")