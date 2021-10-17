def send_messages(messages, sent_messages):
    while messages:
        print("\nMoving message:")
        message = messages.pop()
        print(message)
        sent_messages.append(message)

sent_messages = []
messages = ['Hi Ingrid!', 'Hi Erlend', 'Goodbye Andrew.']

send_messages(messages[:],sent_messages)

print(messages)
print(sent_messages)