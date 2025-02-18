cnt = 0
def F(n):
    if n <= 2:
        return n
    if n % 2 == 0 and n > 2:
        return n + 6 * F(n - 2)
    if n % 2 != 0 and n > 2:
        return 2 * n *n + F(n - 2)
for i in range (1, 200):
    if F(i) % 4 == 0:
        cnt += 1
print(cnt)