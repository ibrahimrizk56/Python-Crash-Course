# 5-1. Conditional Tests: Write a series of conditional tests. Print a
# statement describing each test and your prediction for the results of each
# test. Your code should look something like this:
# car = 'subaru' 
# print("Is car == 'subaru'? I predict True.") 
# print(car == 'subaru') 
# print("\nIs car == 'audi'? I predict False.") 
# print(car == 'audi')
# Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# Create at least 10 tests. Have at least 5 tests evaluate to True and another 5
# tests evaluate to False.


car = 'bmw'

#test 1 
print("Is car == 'bmw'? I predict True.")
print(car == 'bmw')

#test 2 
print("Is car == 'audi'? I predict False.")
print(car == 'audi')
print("")

status = True

#test 3 
print("Is status = True? I predict True.")
print(status == True)

#test 4
print("Is status = True ? I predict False.")
print(status == False)
print("")

number = 10

#test 5 
print("Is number == 10? I predict True.")
print(number == 10)

#test 6
print("Is number == 10? I predict False.")
print(number != 10)
print("")

#test 7
print("Is number < 10? I predict True.")
print(number < 10)

#test 8
print("Is number < 10? I predict false")
print(number >= 10)
print("")

#test 9
print("Is number > 10? I predict True.")
print(number > 10)

#test 10
print("Is number > 10? I predict False.")
print(number <= 10)
print("") 