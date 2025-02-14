s = 654 ** 25 + 927 ** 13 + 243 ** 5 - 44 ** 2 + 2025
n = 0
alf = "0123456789ABCDEFGHIJKLMNO"
while s > 0:
    if s % 25 > 9:
        n+=1
    s = s//25
print(n)