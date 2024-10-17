# Chapter 9/Restaurant.py

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
    
restaurant = Restaurant('Three Generations', 'seafood')
print(restaurant.name)
print(restaurant.cuisine)

restaurant.describe_restaurant()
restaurant.open_restaurant()