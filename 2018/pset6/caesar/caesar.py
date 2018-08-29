from cs50 import get_string
import sys

key = int(sys.argv[1]) % 26
if key > 0:
    pt = get_string("plaintext: ")
    print("ciphertext: ", end='')
    for c in pt:
        if c.isalpha():
            if c.isupper():
                print(chr(ord(c) + key - 26) if ord(c) + key > 90 else chr(ord(c) + key), end='')
            else:
                print(chr(ord(c) + key - 26) if ord(c) + key > 122 else chr(ord(c) + key), end='')
        else:
            print(c, end='')
    print("")
else:
    print("Key must be a non-negative integer.")

