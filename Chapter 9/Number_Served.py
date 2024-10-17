# Chapter 9/Number_Served.py

class Restaurant():


    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        message = f"{self.name} provides {self.cuisine}."
        print(f"\n{message}")
        
    def open_restaurant(self):
        message = f"{self.name} is open. Come."
        print(f"\n{message}")
        
    def set_number_served(self, number_served):
        self.number_served = number_served
        
    def increment_number_served(self, additional_served):
        self.number_served += additional_served
    
restaurant = Restaurant('Three Generations', 'seafood')
# print(restaurant.name)
# print(restaurant.cuisine)

restaurant.describe_restaurant()
# restaurant.open_restaurant()

restaurant.number_served = 0
print("\nIn the morning when the restaurant was opened:")
print(f"\tTotal number of customers served: {restaurant.number_served}")

print("\nBefore afternoon tea-time hours:")
restaurant.number_served = 430
print(f"\tTotal number of customers served: {restaurant.number_served}")

restaurant.set_number_served(1257)
print("\nA mistake was made in counting for lunch hour figure.")
print(f"\tRevised total number of customers served before afternoon tea-time hours: {restaurant.number_served}")

restaurant.increment_number_served(239)
print("\nAdding customers served after tea-time hour to close of play of the day.")
print(f"\t Total number of customers served for whole day: {restaurant.number_served}")
