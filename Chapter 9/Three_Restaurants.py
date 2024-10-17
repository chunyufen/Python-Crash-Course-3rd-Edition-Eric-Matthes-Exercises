# Chapter 9/Three_Restaurants.py

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
    
fat_duck = Restaurant('The Fat Duck', 'French Cuisine')
fat_duck.describe_restaurant()

eleven_madison_park = Restaurant('Eleven Madison Park', 'Thai Cuisine')
eleven_madison_park.describe_restaurant()


el_bulli = Restaurant('El Bulli', 'Italian Cuisine')
el_bulli.describe_restaurant()
