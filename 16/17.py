cnt = 0
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 3 * F(n - 1) - G(n-1)
def G(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * F(n-1) + 2 * G(n-1) +n * n
for i in str(G(4)):
    cnt += int(i)
print(cnt)