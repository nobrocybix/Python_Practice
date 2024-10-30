class Name():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("First name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + "!")

class Admin(Name):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
    
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Administrator's permissions:")

        for privilege in self.privileges:
            print(privilege)


eric = Name("eric", "matthes")
eric.describe_user()
eric.greet_user()

print("\n")

nobrocybix = Admin("Jack", "Oneil")
nobrocybix.describe_user()
nobrocybix.greet_user()
nobrocybix.show_privileges()