# 8-10. Sending Messages: Start with a copy of your program from Exercise
# 8-9. Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


# Original list of messages
text_messages = [
    "Hello, how are you?",
    "Don't forget the meeting at 5.",
    "Happy Birthday!",
    "Call me when you're free."
]

# New empty list
sent_messages = []

# Call the function
send_messages(text_messages, sent_messages)

# Print both lists to verify movement
print("\nOriginal messages list:")
print(text_messages)

print("\nSent messages list:")
print(sent_messages)