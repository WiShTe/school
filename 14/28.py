s = oct(19234 + 465123 - 412 ** 4)[2:]
n = 0
for i in str(s):
    if i in ['1', '3', '5', '7']:
        n += 1
print(n)
