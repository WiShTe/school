s = 281474976710656**22 - 1099511627776**10 - 48**19
n = 0
while s > 0:
    if s % 16 == 11:
        n += 1
    s = s // 16
print(n)