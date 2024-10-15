# Chapter 5/No_Users.py

usernames = ['admin', 'blackacre', 'jane doe', 'john smith', 'john doe']
# usernames = [] # for checking

if usernames:
    for username in usernames:
        if username == usernames[0]:
            print(f"Hello, {username.title()}, would you like to see a status report?")
        else:
            print(f"Hello, {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users")