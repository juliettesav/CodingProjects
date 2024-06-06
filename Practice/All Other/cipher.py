def caesar_shift_char(c, shift):
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - base + shift) % 26 + base)
    return c

def caesar_encode(text, shift):
    return ''.join(caesar_shift_char(c, shift) for c in text)

def caesar_decode(text, shift):
    return caesar_encode(text, -shift)

print()
print("Would you like to encode a secret message or decode a secret message.")
menu = input("Type 'E' to Encode and 'D' to Decode: ")

if menu == "E":
    message = input("Type your message to encrypt: ")
    print(caesar_encode(message, 3))

if menu == "D":
    message = input("Type your message to decode: ")
    print(caesar_decode(message, 3))
    