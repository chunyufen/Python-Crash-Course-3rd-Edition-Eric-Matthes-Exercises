# Chapter 6/Polling.py

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle'] # coders who have and who have not taken the poll

favorite_languages = {
      'jen': 'python',
      'sarah': 'c',
      'edward': 'rust',
      'phil': 'python',
      'john': 'java',
      'jane': 'sql',
      'blackacre': 'go',
      } # those who have taken the poll and the favorite language was therefore known.

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you for taking the poll, {coder.title()}!")
    else:
        print(f"{coder.title()}, you have not taken the poll. Please take the poll. It consists of 1 question.  What's your favorite programming language?")
