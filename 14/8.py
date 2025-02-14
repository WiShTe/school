s = bin(64 ** 2023 + 32 ** 2022 - 8 **2021 - 2)
n = 0
for i in s[2:]:
    n += int(i)
print(hex(n))
