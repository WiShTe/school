s = 127342 + 399340 - 29 ** 3
n = 0
while s > 0: 
    if s % 16 > 9:
        n += 1
    s = s//16
print(n)