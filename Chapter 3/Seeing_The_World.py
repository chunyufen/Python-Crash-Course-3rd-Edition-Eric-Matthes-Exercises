# Chapter 3/Seeing_The_World.py
locations = ["united states", "new zealand", "canada", "shangtong", "xianjiang"]
print("This is the original list:")
print(locations)
print("\nThis is the sorted list without modifying the original list:")
print(sorted(locations))
print("\nThis is the original list again:")
print(locations)

print("\nThis is the list in reverse order:")
locations.reverse()
print(locations)

print("\nThis is the original list again:")
locations.reverse()
print(locations)

print("\nThis is the sorted list modifying the original list:")
locations.sort(reverse=True)
print(locations)
