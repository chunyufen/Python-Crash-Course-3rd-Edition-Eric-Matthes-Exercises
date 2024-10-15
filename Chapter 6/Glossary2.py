# Chapter 6/Glossary2.py

program_words= {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
}

for key, value in program_words.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    
for program_word, meaning in program_words.items(): # using 2 strings to represent key and value
    print(f"\n{program_word.title()} means {meaning}")
    
