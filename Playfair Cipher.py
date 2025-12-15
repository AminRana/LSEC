# List of alphabets (excluding 'j')
alphabet_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']

# Convert string to lowercase
def make_lower(text):
    return text.lower()

# Remove spaces from string
def strip_spaces(text):
    return "".join([ch for ch in text if ch != " "])

# Group characters into pairs
def make_pairs(text):
    pairs = []
    start = 0
    for i in range(2, len(text), 2):
        pairs.append(text[start:i])
        start = i
    pairs.append(text[start:])
    return pairs

# Insert filler letter 'x' if duplicate letters appear in a pair
def insert_filler(text):
    length = len(text)
    if length % 2 == 0:
        for i in range(0, length, 2):
            if text[i] == text[i+1]:
                new_word = text[:i+1] + 'x' + text[i+1:]
                return insert_filler(new_word)
        return text
    else:
        for i in range(0, length-1, 2):
            if text[i] == text[i+1]:
                new_word = text[:i+1] + 'x' + text[i+1:]
                return insert_filler(new_word)
        return text

# Generate 5x5 key matrix
def build_matrix(key_word, alphabet_set):
    key_letters = []
    for ch in key_word:
        if ch not in key_letters:
            key_letters.append(ch)

    matrix_elements = key_letters[:]
    for ch in alphabet_set:
        if ch not in matrix_elements:
            matrix_elements.append(ch)

    matrix = []
    while matrix_elements:
        matrix.append(matrix_elements[:5])
        matrix_elements = matrix_elements[5:]
    return matrix

# Search for element in matrix
def locate(matrix, element):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == element:
                return i, j

# Row rule
def row_encrypt(matrix, r1, c1, r2, c2):
    char1 = matrix[r1][(c1+1) % 5]
    char2 = matrix[r2][(c2+1) % 5]
    return char1, char2

# Column rule
def col_encrypt(matrix, r1, c1, r2, c2):
    char1 = matrix[(r1+1) % 5][c1]
    char2 = matrix[(r2+1) % 5][c2]
    return char1, char2

# Rectangle rule
def rect_encrypt(matrix, r1, c1, r2, c2):
    char1 = matrix[r1][c2]
    char2 = matrix[r2][c1]
    return char1, char2

# Playfair encryption
def playfair_encrypt(matrix, pairs):
    cipher_list = []
    for pair in pairs:
        r1, c1 = locate(matrix, pair[0])
        r2, c2 = locate(matrix, pair[1])

        if r1 == r2:
            ch1, ch2 = row_encrypt(matrix, r1, c1, r2, c2)
        elif c1 == c2:
            ch1, ch2 = col_encrypt(matrix, r1, c1, r2, c2)
        else:
            ch1, ch2 = rect_encrypt(matrix, r1, c1, r2, c2)

        cipher_list.append(ch1 + ch2)
    return "".join(cipher_list)

# Main program
if __name__ == "__main__":
    # User input
    plain_input = input("Enter the plaintext: ")
    key_input = input("Enter the key: ")

    # Preprocess plaintext
    plain_input = strip_spaces(make_lower(plain_input))
    plain_input = insert_filler(plain_input)
    pairs = make_pairs(plain_input)
    if len(pairs[-1]) != 2:
        pairs[-1] += 'z'

    # Build matrix
    key_input = make_lower(key_input)
    matrix = build_matrix(key_input, alphabet_set)

    # Encrypt
    cipher_text = playfair_encrypt(matrix, pairs)

    print("Key:", key_input)
    print("Plaintext:", plain_input)
    print("Ciphertext:", cipher_text)
