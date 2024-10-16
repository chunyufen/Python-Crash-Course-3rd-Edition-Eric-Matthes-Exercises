# Chapter 8/Archived_Messages.py

def show_messages(messages):
    """Print all messages in the original list."""
    print("\nShowing all messages before sending out:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages): # this function involves 2 arguments
    """Print (send) each message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while messages: # while messages is not empty
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ['the demonstration you requested is scheduled for today', 'we have sent over the program details you requested', 'welcome to our computer laboratory', 'ready to get started?']

show_messages(messages)

converted_messages = [message.capitalize() for message in messages]

show_messages(converted_messages)

sent_messages = []
send_messages(converted_messages[:], sent_messages) # The slice notation [:] makes a copy of the list to send to the function. If we didn\'t want to empty the list of "converted_messages"

print("\n----------")
print("\nFinal List")
print("\n----------")
print(messages) # showing the original list is empty
print("\n")
print(sent_messages) # showing the sent list