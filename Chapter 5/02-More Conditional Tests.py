# 5-2. More Conditional Tests: You don’t have to limit the number of tests
# you create to 10. If you want to try more comparisons, write more tests and
# add them to conditional_tests.py. Have at least one True and one False result
# for each of the following:
# Tests for equality and inequality with strings
# Tests using the lower() method
# Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to
# Tests using the and keyword and the or keyword
# Test whether an item is in a list
# Test whether an item is not in a list

#string test
car = 'BMW'

if car.lower == 'bmw':
    print(f"my car is BMW.")
else:
    print("my car is not BMW")
print("")

#Numerical test
number = 10

if number < 10 :
    print("number is less than 10.")
else:
    print("number is greater than or equal 10.")
print("")

number_1 = 15

if number == 10 and number_1 != 10: #same condition but with or   
    print(f"number = 10\nnumber_1 = 15")
else:
    print("there was an error.")
print("")

list = ['car' , 'train']

if 'train' in list:
    print("i love train")
else:
    print("i love car.")
print("")