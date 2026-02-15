# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

message = "Enter 'quit' when you are finished."
message += '\nplease enter a pizza topping to add: '

while True:
    topping = input(message)
    if topping == 'quit':
        break
    else:
        print(f"adding {topping} to your pizza...")