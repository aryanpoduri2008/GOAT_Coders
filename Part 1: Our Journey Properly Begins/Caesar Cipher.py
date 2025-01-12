"""
Program that encodes a message using the caesar cipher
    - Asks for a message and shift number
    - Shifts the message using chr() and ord()
    - Prints the encoded message

Ex:
Message: "My name is Bob"
Shift Number: 2
Encoded Message: "Oa pcog ku Dqd"
"""

print("Welcome to the Secret Code Program!")

message = input("Enter a message to encode: ")
shift = int(input("Enter the shift number (1 to 25): "))

encoded_message = ""
for letter in message:
    if letter.isupper():
        encoded_message += chr((ord(letter) + shift - 65) % 26 + 65)
    elif letter.islower():
        encoded_message += chr((ord(letter) + shift - 97) % 26 + 97)
    else:
        encoded_message += letter

print("Here is the encoded message: " + encoded_message)
# To decode it just do -shift