# Chapter 4/Buffet.py

buffet = ('salad', 'soup', 'vegetables', 'fruits', 'fish')

print("Here are the type of food available in a buffet:")
for food in buffet:
    print(food)

print(""" 
buffet.insert('meat') # example of wrong code
buffet[0] = 'meat' # example of wrong code
""")

buffet_list = list(buffet) # change from tuple to list

buffet_list.append('pork') # can only append one by one
buffet_list.append('beef')
# buffet_list = ('salad', 'soup', 'vegetables', 'fruits', 'fish', 'pork', 'beef')
buffet = buffet_list
print("Buffet has been updated:")
for food in buffet:
    print(food)