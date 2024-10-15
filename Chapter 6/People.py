# Chapter 6/People.py

people = []

person = {
    'first_name': 'john',
    'last_name': 'doe',
    'age': 21,
    'city': 'texas',
}

people.append(person)

person = {
    'first_name': 'jane',
    'last_name': 'doe',
    'age': 22,
    'city': 'new york',
}

people.append(person)

person = {
    'first_name': 'richard',
    'last_name': 'roe',
    'age': 23,
    'city': 'new orleans',
}

people.append(person)


person = {
    'first_name': 'jane',
    'last_name': 'roe',
    'age': 24,
    'city': 'mississippi',
}

people.append(person)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    print(f"{name}, of {city}, is {age} years old.")