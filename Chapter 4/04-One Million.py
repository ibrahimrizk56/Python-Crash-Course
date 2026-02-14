# 4-4. One Million: Make a list of the numbers from one to one million, and
# then use a for loop to print the numbers. (If the output is taking too long,
# stop it by pressing CTRL-C or by closing the output window.)

#generate a list from 1 to 1,000,000
numbers = list(range(1,1_000_001))

#doing a for loop to print from 1 to 1,000,000
for number in numbers:
    print(number)