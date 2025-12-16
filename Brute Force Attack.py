# Brute force attack on Caesar cipher with user input

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - base - shift) % 26 + base)
        else:
            plaintext += char
    return plaintext

# Ask the user to enter ciphertext
ciphertext = input("Enter the ciphertext: ")

print("\nAttempting brute force attack...\n")

# Try all possible shifts (0–25)
for shift in range(26):
    possible_plaintext = caesar_decrypt(ciphertext, shift)
    print(f"Shift {shift}: {possible_plaintext}")


