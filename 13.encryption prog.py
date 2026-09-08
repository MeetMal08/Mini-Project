# Python Encryption Program

import random
import string

chars = string.whitespace + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()
random.shuffle(key)
print(f"Characters: {chars}")
print(f"Key: {key}")

#ENCRYPTION
plain_text = input("Enter the text to encrypt: ")
cipher_text = ""

for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

print(f"Encrypted text: {cipher_text}")
print(f"original text: {plain_text}")

