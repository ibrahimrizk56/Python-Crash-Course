# 3-10. Every Function: Think of things you could store in a list. For
# example, you could make a list of mountains, rivers, countries, cities,
# languages, or anything else you’d like. Write a program that creates a list
# containing these items and then uses each function introduced in this
# chapter at least once.

names = ['ezz', 'mohamed', 'ahmed']

# Print original list
print("Original list:")
print(names)
print("------------------------------------------")

# Append method
names.append('ibrahim')
print("After append:")
print(names)
print("------------------------------------------")

# Insert method
names.insert(0, 'samir')
print("After insert:")
print(names)
print("------------------------------------------")

# Remove method
names.remove('ezz')
print("After remove:")
print(names)
print("------------------------------------------")

# Pop method
popped_name = names.pop()
print(f"Popped name: {popped_name}")
print("After pop:")
print(names)
print("------------------------------------------")

# del statement
del names[0]
print("After del:")
print(names)
print("------------------------------------------")

# Length of list
print(f"Length of list: {len(names)}")
print("------------------------------------------")

# Temporary sorted list
print(f"Temporary sorted list: {sorted(names)}")
print(f"Original list remains: {names}")
print("------------------------------------------")

# Permanent sort
names.sort()
print("After permanent sort:")
print(names)
print("------------------------------------------")

# Reverse
names.reverse()
print("After reverse:")
print(names)