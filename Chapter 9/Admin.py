# Chapter 9/Admin.py

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

        """
        next steps:
        init parents def
        super (copy) parents def without self
        add attribute or attributes for new class (self.xxxx =)
        define to show the new attribute
        """

class Admin(User):
    
    def __init__(self, first_name, last_name, username, email, telephone, location):
        super().__init__(first_name, last_name, username, email, telephone, location) # don't mention self again in super
        self.privileges = [] # add an attribute privileges
        
    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges: # is not empty
            for privilege in self.privileges:
                print(f"-{privilege}")
        else:
            print("-This user has no privileges.")
            
john = Admin('john', 'doe', 'john1997', 'john_doe@example.com', 4037807890, 'canada')
john.describe_user()

john_privileges = [
    'reset password',
    'read all discussions',
    'suspend accounts',
    'activate accounts',
]

john.show_privileges()
