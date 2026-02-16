# 8-9. Messages: Make a list containing a series of short text messages. Pass
# the list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    for message in messages:
        print(message)


# Create a list of text messages
text_messages = [
    "Hello, how are you?",
    "Don't forget the meeting at 5.",
    "Happy Birthday!",
    "Call me when you're free."
]

print("Showing messages:")
show_messages(text_messages)