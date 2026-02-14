# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to
# print the numbers in your list.

#generate a list from 3 to 30 (multiples of 3)
threes = [value*3 for value in range(3,31)]
print(threes)

#doing a for loop to print numbers in list
for multiple_of_three in threes:
    print(multiple_of_three)