# Chapter 9/Battery_Upgrade.py

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

        """
        the above is the final version of electric_car.py in the book section
        """
        
    def upgrade_battery(self):
        """check the battery size and set the capacity to 65 if it isn\'t already."""
        if self.battery_size == 40:
            self.battery_size = 65
            print("Batter was upgraded to 65 kWh.")
        else:
            print("The battery has already been upgraded.")
        
        """
        Make an electric car with a default battery size
        """
        
class Electric_Car(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery() # using the class battery
        
print("Make an electric car, and check the range:")
motorhome = Electric_Car('toyota', 'camper van', 2024)
motorhome.battery.get_range()
print("\nUpgrade the battery, and check the range again:")
motorhome.battery.upgrade_battery()
motorhome.battery.get_range()

