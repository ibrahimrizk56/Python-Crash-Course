# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

person_1 = {'first_name' : 'hamada' , 'last_name' : 'sabry' , 'age' : 21 , 'city' : 'aga'}
person_2 = {'first_name' : 'hatem' , 'last_name' : 'mousa' , 'age' : 21 , 'city' : 'talkha'}
person_3 = {'first_name' : 'ibrahim' , 'last_name' : 'ahmed' , 'age' : 21 , 'city' : 'mansoura'}

people = [person_1 , person_2 , person_3]

for person in people:
    print(f"name: {person['first_name']} {person['last_name']}")
    print(f"age: {person['age']}")
    print(f"city: {person['city']}\n")