import sys
import crypt

if len(sys.argv) != 2:
    sys.exit(1)

#set all chars in a list
chrs = []
for i in range(52):
    if i < 26:
        chrs.append(chr(65 + i))
    else:
        chrs.append(chr(71 + i))

# get input ready to check
encryptKey = sys.argv[1]
# salt is the first two characters of hashed password
salt = encryptKey[0:2]
# array position and chr index
ap0 = 0

while True:
    p = chrs[ap0]
    ap0 += 1
    print(p)
    if encryptKey == crypt.crypt(p, salt):
        print(f"password: {p}")
        sys.exit(0)
    if ap0 > 51:
        break

ap0, ap1 = 0, 0
while True:
    p = chrs[ap0] + chrs[ap1]
    ap0 += 1
    print(p)
    if encryptKey == crypt.crypt(p, salt):
        print(f"password: {p}")
        sys.exit(0)
    if ap0 > 51:
        ap0 = 0
        ap1 += 1
        if ap1 > 51:
            break


ap0, ap1, ap2 = 0, 0 ,0
while True:
    p = chrs[ap0] + chrs[ap1] + chrs[ap2]
    ap0 += 1
    print(p)
    if encryptKey == crypt.crypt(p, salt):
        print(f"password: {p}")
        sys.exit(0)
    if ap0 > 51:
        ap0 = 0
        ap1 += 1
        if ap1 > 51:
            ap1 = 0
            ap2 += 1
            if ap2 > 51:
                break

ap0, ap1, ap2, ap3 = 0, 0 ,0, 0
while True:
    p = chrs[ap0] + chrs[ap1] + chrs[ap2] + chrs[ap3]
    ap0 += 1
    print(p)
    if encryptKey == crypt.crypt(p, salt):
        print(f"password: {p}")
        sys.exit(0)
    if ap0 > 51:
        ap0 = 0
        ap1 += 1
        if ap1 > 51:
            ap1 = 0
            ap2 += 1
            if ap2 > 51:
                ap2 = 0
                ap3 += 1
                if ap3 > 51:
                    break