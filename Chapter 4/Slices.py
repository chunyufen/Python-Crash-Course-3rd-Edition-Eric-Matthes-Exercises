# Chapter 4/Slices.py

hills = ['amne machin', 'badaling', 'paektu mountain', 'baishi mountain', 'baiyun mountain', 'tomort', 'zimao mountain', 'kunyu mountain', 'changbai mountains']

print(hills)
print(f"There are {len(hills)} items in the list")


print("The first three items in the list are:")
for hill in hills[:3]:
    print(hill.title())
    
print("The three items starting from the middle are:")
for hill in hills[5:]:
    print(hill.title())
    
print("The last three items are:")
for hill in hills[-3:]:
    print(hill.title())

