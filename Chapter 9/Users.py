# Chapter 9/Users.py

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, telephone, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.telephone = telephone
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Telephone: {self.telephone}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back to our website, {self.username}!")

john = User('john', 'doe', 'john1997', 'john_doe@example.com', 4037807890, 'canada')
john.describe_user()
john.greet_user()

jane = User('jane', 'roe', 'janeroe', 'jane1997@example.com', 4169486623, 'alaska')
jane.describe_user()
jane.greet_user()