from cs50 import get_int

while True:
    n = get_int("Number: ")
    if n >= 0:
        break

typ = 0
if len(str(n)) == 15:
    am = str(n)[0:2]
    if am == "34" or am == "37":
        typ = 1
elif len(str(n)) == 13:
    if str(n)[0:1] == "4":
        typ = 2
elif len(str(n)) == 16:
    j = n // 10 ** 14
    if j >= 51 and j <= 55:
        typ = 3
    elif j >= 40 and j <= 49:
        typ = 2

if typ > 0:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10

        bytwo = (n % 10) * 2
        if bytwo >= 10:
            bytwo = bytwo % 10 + 1
        s += bytwo
        n //= 10

    if s % 10 != 0:
        typ = 0

if typ == 0:
    print("INVALID")
elif typ == 1:
    print("AMEX")
elif typ == 2:
    print("VISA")
elif typ == 3:
    print("MASTERCARD")