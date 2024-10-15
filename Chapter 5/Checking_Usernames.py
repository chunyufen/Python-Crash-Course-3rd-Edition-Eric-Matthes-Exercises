# Chapter 5/Checking_Usernames.py

current_users = ['admin', 'blackacre', 'jane doe', 'john smith', 'john doe']

new_users = ['Blackacre', 'Jane Doe', 'richard roe', 'fnu lnu', 'jane roe']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user.title()}, the username has already been used.")
    else:
        print(f"{new_user.title()}, the username is available.")