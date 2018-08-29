from cs50 import get_string
import sys

if len(sys.argv) > 2:
    sys.exit(1)

key = sys.argv[1]
if key.isalpha():
    key = key.upper()
else:
    print("has non-alphabetical character")
    sys.exit(1)

pt = get_string("plaintext:  ")
print("ciphertext: ", end='')

#print(key)
i = 0
for c in pt:
    if c.isalpha():
        m = ord(key[i]) - ord('A')
        if c.isupper():
            print(chr(ord(c) + m - 26) if ord(c) + m > 90 else chr(ord(c) + m), end='')
        else:
            print(chr(ord(c) + m - 26) if ord(c) + m > 122 else chr(ord(c) + m), end='')
        i += 1
        if i == len(key):
            i = 0
    else:
        print(c, end='')
print("")

