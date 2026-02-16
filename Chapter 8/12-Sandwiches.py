# 8-12. Sandwiches: Write a function that accepts a list of items a person
# wants on a sandwich. The function should have one parameter that collects
# as many items as the function call provides, and it should print a summary
# of the sandwich that’s being ordered. Call the function three times, using a
# different number of arguments each time.

def make_sandwich(*items):
    """Print a summary of the sandwich being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

# Function calls with different numbers of arguments
make_sandwich("turkey")
make_sandwich("ham", "cheese")
make_sandwich("lettuce", "tomato", "onion", "mayonnaise")