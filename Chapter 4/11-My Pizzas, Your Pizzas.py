# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do
# the following:
# Add a new pizza to the original list.
# Add a different pizza to the list friend_pizzas.
# Prove that you have two separate lists. Print the message My favorite pizzas
# are:, and then use a for loop to print the first list. Print the message My
# friend’s favorite pizzas are:, and then use a for loop to print the second list.
# Make sure each new pizza is stored in the appropriate list.

#list of pizzas
pizzas = ['Cheese' , 'Pepperoni' , 'Margherita']

#copy of list of pizzas to list of friend_pizzas
friend_pizzas = pizzas[:] 
#friend_pizzas = pizzas is wrong
#(will make them the same list any chage happen to any one both will change)

#adding a new pizza to pizzas list
pizzas.append('Neapolitan')

#adding a different pizza to friend_pizzas
friend_pizzas.append('Marinara')

#print my pizzas and my friend pizzas
print("My favorite pizzas are:")
print(pizzas)

print("My friend’s favorite pizzas are:")
print(friend_pizzas)