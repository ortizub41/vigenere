# Generate the alphabet needed
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '.', ',', '?'
            ]

# Storage for the encrypted message
cipher = []

# Obtain the message, make it uppercase, get rid of spaces
message = raw_input("Enter a message:\n").upper().replace(" ", "")

# Obtain the key, make it uppercase, get rid of spaces
key = raw_input("Enter a key word:\n").upper().replace(" ", "")

# Make the keyword the same length as the message
for character in message:
    if len(key) < len(message):
        key *= 2
    key = key[:len(message)]

# Find out the positions of the message/key letters
for i in range(len(message)):
    # Enumerate message/key positions
    message_position = [a for a, x in enumerate(alphabet) if x == message[i]]
    key_position = [b for b, p in enumerate(alphabet) if p == key[i]]

    # Generate the positions of the message and key
    message_key_positions = message_position + key_position

    # Add the positions of the message and key characters
    addition = message_key_positions[0] + message_key_positions[1]

    # Find the first part of the alphabet
    alphabet_first = alphabet[:key_position[0]]

    # Find the last part of the alphabet
    alphabet_last = alphabet[key_position[0]:]

    # Concatenate the last and first part of the alphabet
    alphabet_appended = alphabet_last + alphabet_first

    # Append the encrypted message to cipher
    cipher.append(alphabet_appended[message_position[0]])

print "Your encrypted message is:"

# print the encrypted message
for i in range(len(cipher)):
    print cipher[i],
