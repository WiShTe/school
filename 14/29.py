s = 456223 + 77707 - 51249
alf = "0123456789ABCDEFGHIJKLMNO"
num = ""
while s > 0:
    num += alf[s % 25]
    s = s // 25
print(num[::-1])
