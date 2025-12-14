import random

import string

chars=" "+string.punctuation+string.digits+string.ascii_letters

chars=list(chars)

key=chars.copy()

random.shuffle(key)

# ENVRYPT

plain_text=input("enter the string to encrypt:")

cypher_text=""

for letter in plain_text:
    index=chars.index(letter)
    cypher_text+=key[index]
print(f"the origional text is:{plain_text}")
print(f"the encrypted text is:{cypher_text}")

#DECRYPT

cypher_text=input("enter the string to decrypt:")

plain_text=""

for letter in cypher_text:
    index=key.index(letter)
    plain_text+=chars[index]
print(f"the origional text is:{cypher_text}")
print(f"the encrypted text is:{plain_text}")