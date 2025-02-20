f = [0] * 1000
for n in range(1, 1000):
    if n < 3:
        f[n] = 1
    if n > 3:
        f[n] = f[n - 2] * (n // 3)
print(f[16])