def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift letters
            # Handle uppercase and lowercase separately
            base = ord('A') if char.isupper() else ord('a')
            # Shift within alphabet range
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    return result

# User input
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_cipher(message, shift)
print("Encrypted message:", encrypted)

