# 3-6. More Guests: You just found a bigger dinner table, so now more space
# is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

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