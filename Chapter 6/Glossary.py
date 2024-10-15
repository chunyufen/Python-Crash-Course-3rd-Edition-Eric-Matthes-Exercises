# Chapter 6/Glossary.py

program_words= {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
}

key_to_print = 'string' # 'string' is called key; 'a series of characters' is the value corresponding the key; referring to the key will give the value. 
print(f"\n{key_to_print.title()}: {program_words[key_to_print]}")

key_to_print = 'comment'
print(f"\n{key_to_print.title()}: {program_words[key_to_print]}")

key_to_print = 'list'
print(f"\n{key_to_print.title()}: {program_words[key_to_print]}")

key_to_print = 'loop'
print(f"\n{key_to_print.title()}: {program_words[key_to_print]}")

key_to_print = 'dictionary'
print(f"\n{key_to_print.title()}: {program_words[key_to_print]}")



