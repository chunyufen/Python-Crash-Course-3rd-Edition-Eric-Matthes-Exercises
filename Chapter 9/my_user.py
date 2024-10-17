# Chapter 9/my_user.py

from user import Admin

john = Admin('john', 'doe', 'john1997', 'john_doe@example.com', 4037807890, 'canada')
john.describe_user()

john_privileges = [
    'reset password',
    'read all discussions',
    'suspend accounts',
    'activate accounts',
]

john.privileges.privileges = john_privileges

print(f"\nThe admin {john.username} has these privileges: ")
john.privileges.show_privileges()