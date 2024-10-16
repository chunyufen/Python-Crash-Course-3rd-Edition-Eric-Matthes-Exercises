# Chapter 7/Three_Exists.py

# 3 possible answers

prompt  = "\nwhat tappings would you like for your pizza?"
prompt += "\nEnter 'quit' when you finished: "
topping = ""
active = True
while active:
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
    else:
        break


"""
prompt  = "\nwhat tappings would you like for your pizza?"
prompt += "\nEnter 'quit' when you finished: "
topping = ""
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")
"""

"""
prompt  = "\nwhat tappings would you like for your pizza?"
prompt += "\nEnter 'quit' when you finished: "
topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(topping)
"""