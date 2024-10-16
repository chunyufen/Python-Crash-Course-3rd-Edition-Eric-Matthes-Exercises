# Chapter 8/Messages.py

def show_messages(messages):
    print("\nShowing all messages:")
    for message in messages:
        print(message)
        
messages = ['the demonstration you requested is scheduled for today', 'we have sent over the program details you requested', 'welcome to our computer laboratory', 'ready to get started?']

show_messages(messages)

# first way to capitalize

capitalized_messages = []
for message in messages:
    capitalized_messages.append(message.capitalize())

show_messages(capitalized_messages)

# second way to capitalize

converted_messages = [message.capitalize() for message in messages]
print(converted_messages)