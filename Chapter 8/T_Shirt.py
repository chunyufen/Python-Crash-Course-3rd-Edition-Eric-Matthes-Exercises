# Chapter 8/T_Shirt.py

def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} T-shirt.")
    print(f'It will be printed with, "{message}"')

make_shirt('large', 'I love Python!')
make_shirt(message ="Readability counts.", size ='medium')
make_shirt(size ='small', message ='Simple is better than complex.')   