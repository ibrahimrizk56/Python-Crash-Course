# 4-5. Summing a Million: Make a list of the numbers from one to one
# million, and then use min() and max() to make sure your list actually starts at
# one and ends at one million. Also, use the sum() function to see how quickly
# Python can add a million numbers.

#generate list from 1 to 1,000,000
numbers = list(range(1,1_000_001))

#printing minimum and maximum and summation 
print(f"minimum value = {min(numbers)}")
print(f"maximum value = {max(numbers)}")
print(f"summation of values = {sum(numbers)}")