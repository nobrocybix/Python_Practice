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

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, num_customesrs_served=0):
        
        super().__init__(restaurant_name, cuisine_type, num_customesrs_served)
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint Chocolate Chip',
           'Coffee', 'Matcha', 'Caramel', 'Hazelnut', 'Coconut', 'Blueberry']
    
    def ice_scream(self):

        print(self.restaurant_name + ' can offer the following ice cream flavors:')
        for flavor in self.flavors:
            print(flavor)


restaurant = Restaurant('Sabatini Ristorante Italiano', 'Italian Restaurant')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print('\n')

restaurant = Restaurant('Haruka', 'Japanese Restaurant', 12)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served()
restaurant.increment_number_served(8)
restaurant.increment_number_served(12)

print('\n')

restaurant = IceCreamStand('Xoco Mexican', 'Italian Restaurant')
restaurant.ice_scream()