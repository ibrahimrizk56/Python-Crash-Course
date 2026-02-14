# 6-4. Glossary 2: Now that you know how to loop through a dictionary,
# clean up the code from Exercise 6-3 (page 99) by replacing your series of
# print() calls with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

glossary = {
    'min()' : 'get minimum value in a list' ,
    'max()' : 'get maximun value in a list' ,
    'sum()' : 'get summation of all values in a list' ,
    'lower()' : 'lowercase all letters in a word' ,
    'upper()' : 'uppercase all letters in a word'
    }

for method, meaning in glossary.items():
    print(f"{method} :\n{meaning}")