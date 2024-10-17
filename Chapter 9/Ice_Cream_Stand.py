# Chapter 9/Ice_Cream_Stand.py

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
        
class Ice_Cream_Stand(Restaurant): # name of parent class in brackets
    
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type) # no need to mention self again
        self.flavors = [] # define self.xxx like the mother
        
    def show_favors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

three_generations = Ice_Cream_Stand('Three Generations')
three_generations.flavors = ['sherbet', 'sorbet', 'frozen yogurt', 'mochi', 'gelato']


three_generations.describe_restaurant()
three_generations.show_favors()

    

