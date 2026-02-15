# 7-2. Restaurant Seating: Write a program that asks the user how many
# people are in their dinner group. If the answer is more than eight, print a
# message saying they’ll have to wait for a table. Otherwise, report that their
# table is ready.

guests = input("how many people are in your dinner group:")
guests = int(guests)


if guests > 8 :
    print("you’ll have to wait for a table.")
else:
    print("your table is ready.")