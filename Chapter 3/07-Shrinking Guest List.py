# 3-7. Shrinking Guest List: You just found out that your new dinner table
# won’t arrive in time for the dinner, and now you have space for only two
# guests.
# Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names
# remain in your list. Each time you pop a name from your list, print a
# message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end of
# your program.

guests = ['ahmed' , 'hatem' , 'hamada']

#print invites
print(f"Hey {guests[0]}, I would like to invite you to dinner.")
print(f"Hey {guests[1]}, I would like to invite you to dinner.")
print(f"Hey {guests[2]}, I would like to invite you to dinner.")
print("-------------------------------------------------------")

#add samir and ezz to the list by the insert method
guests.insert(0 , 'samir')
guests.insert(2 , 'ezz')

#append moaaz to the end of the list by the append method
guests.append('moaaz')

#print invites for samir, ahmed, ezz, hatem, hamada and moaaz
print(f"Hey {guests[0]}, I would like to invite you to dinner.")
print(f"Hey {guests[1]}, I would like to invite you to dinner.")
print(f"Hey {guests[2]}, I would like to invite you to dinner.")
print(f"Hey {guests[3]}, I would like to invite you to dinner.")
print(f"Hey {guests[4]}, I would like to invite you to dinner.")
print(f"Hey {guests[5]}, I would like to invite you to dinner.")
print("-------------------------------------------------------")

#i can only invite two persons
print("I can invite only two people for dinner")

#removing the last four guests fron list
#print sorry messages
print(f"I'm sorry {guests.pop()} I can’t invite you to dinner.")
print(f"I'm sorry {guests.pop()} I can’t invite you to dinner.")
print(f"I'm sorry {guests.pop()} I can’t invite you to dinner.")
print(f"I'm sorry {guests.pop()} I can’t invite you to dinner.")

#print invites for the two persons 
print(f"{guests[0]}, You are still invited.")
print(f"{guests[1]}, You are still invited.")

#removing all guests from guests list
del guests[1]
del guests[0]

#print empty list
print(guests)