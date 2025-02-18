cnt = 0
def F(n):
    if n <= 4:
        return n
    if n > 4 and n % 3 == 0:
        return F(n-1)
    if n > 4 and n % 3 != 0:
        return n * n * n + F(n-3)
for i in range (1, 501):
    if F(i) % 8 == 0:
        cnt += 1
print(cnt)