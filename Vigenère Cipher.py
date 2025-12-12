def vigenere_encrypt(text, key):
    encrypted_text = []
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            # Shift based on key character
            shift = ord(key[key_index % key_length]) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text.append(encrypted_char)
            key_index += 1
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_text.append(char)

    return ''.join(encrypted_text)


def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            # Reverse shift based on key character
            shift = ord(key[key_index % key_length]) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text.append(decrypted_char)
            key_index += 1
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)


# Example usage
text = input("Enter the text: ")
key = input("Enter the key: ")

cipher = vigenere_encrypt(text, key)
print("Encrypted:", cipher)

plain = vigenere_decrypt(cipher, key)
print("Decrypted:", plain)


