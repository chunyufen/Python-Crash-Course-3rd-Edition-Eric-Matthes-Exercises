# Chapter 8/Sandwiches.py

def make_sandwich(*items):
    """Make a sandwich with the given items, some long, some short."""
    print("\nI\'ll make you a great sandwich: ")
    for item in items:
        print(f"by adding {item} to your sandwich.")
    print("Your sandwich is ready!")


make_sandwich('corned beef', 'tuna melt', 'lobster rolls', 'curried chicken')
make_sandwich('pickled egg salad', 'ruben', 'ham and cheese')
make_sandwich('cobb', 'philly cheesesteak')