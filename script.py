import sys
from collections import Counter

if len(sys.argv) != 3:
    print("Usage: python script.py input_file keyword_length")
    print("Example: python script.py cipher.txt 3")
    sys.exit(1)

input_file = sys.argv[1]
length = int(sys.argv[2])
try:
    with open(input_file, 'r') as file:
        cipher = file.read().replace(" ", "").replace("\n", "")
except FileNotFoundError:
    print(f"File '{input_file}' Not Found.")
    sys.exit(1)

cipher_with_spaces = ' '.join(cipher[i:i+length] for i in range(0, len(cipher), length))

groups = []
for i in range(length):
    group = ' '.join(cipher_with_spaces[j] for j in range(i, len(cipher_with_spaces), length+1))
    groups.append(f"Group {i+1}: {group}")

original_letters = ""
for i, group in enumerate(groups):
    print(group)
    group_letters = ''.join(group.split()[1:])
    letter_counts = Counter(group_letters)
    most_common_letter, most_common_count = letter_counts.most_common(1)[0]
    original_letter = chr(ord(most_common_letter) - (length-1))
    print(f"Top Letter : {most_common_letter} ({most_common_count})") 
    print("Original : " + original_letter)
    print()
    original_letters += original_letter

recovered_keyword = "Recovered Keyword: " + original_letters
print(recovered_keyword)


def vigenere_decrypt(ciphertext, keyword):
    decrypted_text = ""
    keyword_length = len(keyword)
    for i, char in enumerate(ciphertext):
        shift = ord(keyword[i % keyword_length]) - ord('A')
        if char.isalpha():
            decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text


decrypted = vigenere_decrypt(cipher, original_letters)
print("\nDecrypted Text:\n" + decrypted)
