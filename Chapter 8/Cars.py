# Chapter 8/Cars.py

def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

awd = make_car('subaru', 'sedan', color='red', engine='diesel', drive='all wheels drive')

print(awd)

motorhome = make_car('toyota', 'camper van', color='white', engine='gas', drive='four wheels drive', year=1991)

print(motorhome)

campervan = make_car('Saic Maxus', 'camper van')

print(campervan)




