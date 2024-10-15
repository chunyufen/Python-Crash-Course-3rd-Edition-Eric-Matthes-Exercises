# Chapter 3/Every_Function.py

mountains = ['Amne Machin', 'Badaling', 'Paektu Mountain', 'Baishi Mountain', 'Baiyun Mountain']


len(mountains)
print(sorted(mountains))
mountains.reverse()
print(mountains)
mountains.sort()
print(mountains)
mountains.sort(reverse=True)
print(mountains)
too_high = 'Baishi Mountain'
mountains.remove(too_high)
print(mountains)
print(f"{too_high} is too high to climb.")
too_wet = mountains.pop(-1)
print(f"{too_wet} is too wet to climb.")
print(mountains)
popped_mountains = mountains.pop() # removing the last item
print(mountains)
del mountains[0] # delete the first one
print(mountains)
mountains.insert(0, 'Mount Hua')
print(mountains)
mountains.insert(-1, 'Jengish Chokusu')
print(mountains)
mountains.append('Labuche Kang')
print(mountains)
print(mountains[3])

