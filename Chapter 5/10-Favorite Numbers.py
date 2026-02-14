# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page
# 98) so each person can have more than one favorite number. Then print
# each person’s name along with their favorite numbers.

favorite_numbers = {
    "Ibrahim": [7, 10, 21],
    "Ali": [3, 8],
    "Sara": [5, 12, 18],
    "Mona": [2],
    "Omar": [9, 14]
}

for name , favorite_numbers_list in favorite_numbers.items():
    print(f"{name} favorite numbers is")
    for favorite_number in favorite_numbers_list:
        print(favorite_number)
    print("")