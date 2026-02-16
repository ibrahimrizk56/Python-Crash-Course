# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call
# the function send_messages() with a copy of the list of messages. After calling
# the function, print both of your lists to show that the original list has
# retained its messages.

# Reset the original list
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

# Empty list for sent messages
sent_messages = []

# Call the function with a COPY of the list
send_messages(text_messages[:], sent_messages)

# Print both lists to verify behavior
print("\nOriginal messages list:")
print(text_messages)

print("\nSent messages list:")
print(sent_messages)