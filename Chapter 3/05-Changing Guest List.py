# 3-5. Changing Guest List: You just heard that one of your guests can’t
# make the dinner, so you need to send out a new set of invitations. You’ll
# have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of
# your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the
# name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in
# your list.

guests = ['ahmed' , 'hatem' , 'hamada']

#print invites
print(f"Hey {guests[0]}, I would like to invite you to dinner.")
print(f"Hey {guests[1]}, I would like to invite you to dinner.")
print(f"Hey {guests[2]}, I would like to invite you to dinner.")

#print that "hatem is busy"
print(f"{guests[1]} is busy.")

#removing hatem and adding bassem
guests[1] = "bassem"

#print invites for ahmed, basssem and hamada
print(f"Hey {guests[0]}, I would like to invite you to dinner.")
print(f"Hey {guests[1]}, I would like to invite you to dinner.")
print(f"Hey {guests[2]}, I would like to invite you to dinner.")