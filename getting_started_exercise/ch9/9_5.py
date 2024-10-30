class Name():
    def __init__(self, first_name, last_name, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        print("First name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


eric = Name("eric", "matthes")
eric.describe_user()
eric.greet_user()

eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(eric.login_attempts)

eric.reset_login_attempts()
print(eric.login_attempts)