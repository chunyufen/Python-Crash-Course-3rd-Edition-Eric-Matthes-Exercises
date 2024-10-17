# Chapter 9/Login_Attempts.py

class User:

    def __init__(self, first_name, last_name, username, email, telephone, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.telephone = telephone
        self.location = location.title()
        self.login_attempts = 0 # need to put it here, cannot put under increment_login_attempts(self), otherwise self.login_attempts will be fixed at 1 ever after attempts 
        
    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"\tUsername: {self.username}")
        print(f"\tEmail: {self.email}")
        print(f"\tTelephone: {self.telephone}")
        print(f"\tLocation: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back to our website, {self.username}!")
    
    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0
        
john = User('john', 'doe', 'john1997', 'john_doe@example.com', 4037807890, 'canada')
john.describe_user()
john.greet_user()

# three login
print("\nMaking 3 login attempts ...")
john.increment_login_attempts()
john.increment_login_attempts()
john.increment_login_attempts()
print(f"\tLogin attempts: {john.login_attempts}")

# reset
print("Resetting login attempts ...")
john.reset_login_attempts()
print(f"\tLogin attempts: {john.login_attempts}")
    
    