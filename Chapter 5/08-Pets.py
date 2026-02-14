# 6-8. Pets: Make several dictionaries, where each dictionary represents a
# different pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your
# list and as you do, print everything you know about each pet.

pets = [
    {
        "animal": "dog",
        "owner": "Ibrahim"
    },
    {
        "animal": "cat",
        "owner": "Mona"
    },
    {
        "animal": "parrot",
        "owner": "Ahmed"
    },
    {
        "animal": "rabbit",
        "owner": "Sara"
    }
]

for pet in pets:
    print(f"animal: {pet['animal']}\nowner: {pet['owner']}\n")