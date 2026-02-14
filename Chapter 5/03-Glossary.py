# 6-3. Glossary: A Python dictionary can be used to model an actual
# dictionary. However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# Print each word and its meaning as neatly formatted output. You might print
# the word followed by a colon and then its meaning, or print the word on one
# line and then print its meaning indented on a second line. Use the newline
# character (\n) to insert a blank line between each word-meaning pair in your
# output.

glossary = {
    'min()' : 'get minimum value in a list' ,
    'max()' : 'get maximun value in a list' ,
    'sum()' : 'get summation of all values in a list' ,
    'lower()' : 'lowercase all letters in a word' ,
    'upper()' : 'uppercase all letters in a word'
    }

print(f"min() :\n{glossary['min()']}")
print(f"max() :\n{glossary['max()']}")
print(f"sum() :\n{glossary['sum()']}")
print(f"lower() :\n{glossary['lower()']}")
print(f"upper() :\n{glossary['upper()']}")