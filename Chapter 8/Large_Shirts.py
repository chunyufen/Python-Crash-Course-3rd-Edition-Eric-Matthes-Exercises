# Chapter 8/Large_Shirts.py

def make_shirt(size ='large', message='I love Python'):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} T-shirt.")
    print(f'It will be printed with, "{message}"')
    
make_shirt() # all default values

make_shirt(size='medium') # medium size though default is large

make_shirt('small', 'If the implementation is hard to explain, it\'s a bad idea.') # totally different from default

