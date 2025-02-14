s = 256 ** 10 * 64 ** 14 + 16 ** 47 - 4
n = 0
while s > 0:
    if s % 4 == 3:
        n += 1
    s = s // 4
print(n)