class Restaurant():

    def __init__(self, restaurant_name, cuisine_type, num_customesrs_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.num_customers_served = num_customesrs_served
        

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name.title() + ".")
        print("The restaurant's cuisine type is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self):
        print("The number of customers served is " + str(self.num_customers_served))

    def increment_number_served(self, num_customers_increased):
        self.num_customers_served += num_customers_increased
        print("I think that the number of customers served is " + str(self.num_customers_served))


restaurant = Restaurant('Sabatini Ristorante Italiano', 'Italian Restaurant')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('Haruka', 'Japanese Restaurant', 12)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served()
restaurant.increment_number_served(8)
restaurant.increment_number_served(12)