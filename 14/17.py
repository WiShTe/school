s = 8 ** 510 + 4 ** 220 - 2 ** 150
n = 0
while s > 0:
    if s % 2 == 1:
        n += 1
    s = s// 2
print(n)