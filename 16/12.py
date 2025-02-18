from sys import setrecursionlimit
setrecursionlimit(3000)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n-1)
print((2026*F(2029)+F(2028))/ F(2027))