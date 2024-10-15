# Chapter 5/Hello_Admin.py

usernames = ['admin', 'tony97', '2024babie', 'root', 'john doe']

for username in usernames:
    if username == usernames[0]:
        print(f"Hello, {username}, would you like to see a status report?")
    else:
        print(f"Hello, {username}, thank you for logging in again.")
    
