# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that
# do each of the following at least once:
# Use a conditional test in the while statement to stop the loop.
# Use an active variable to control how long the loop runs.
# Use a break statement to exit the loop when the user enters a 'quit' value.

message = "Enter 'quit' when you are finished."
message += "\nplease enter your age: "
active = True

while active:
    age = input(message)
    if age == 'quit' :
        break
    elif age == 'stop':
        cont = input("if you want to continue type continue: ")
        active = False
        continue
    else:
        age = int(age)
        if age < 3 :
            print("your ticket is free.")
        elif age >= 3 and age <= 12 :
            print("your ticket is 10$")
        else:
            print("your ticket is 15$")