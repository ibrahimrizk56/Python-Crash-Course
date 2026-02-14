# 6-6. Polling: Use the code in favorite_languages.py (page 96).
# Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have already
# taken the poll, print a message thanking them for responding. If they have
# not yet taken the poll, print a message inviting them to take the poll.

favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'rust', 
    'phil': 'python', 
    } 
non_voters = ['jen' , 'sarah' , 'ahmed' , 'mohamed']

for non_voter in non_voters:
    if non_voter in favorite_languages:
        print(f"{non_voter}, thank you for responding.")
    else:
        print(f"{non_voter},you have not taken the poll.")
        print("please vote from here (https//example.com)\n")