# Chapter 6/Favorite_Places.py

favorite_places = {
    'john doe': ['eiffel tower', 'jaipur', 'colosseum'],
    'jane doe': ['taj mahal', 'acropolis of Athens'],
    'john roe': ['angkor wat', 'golden temple', 'great wall of china']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")