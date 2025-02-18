from sys import setrecursionlimit
setrecursionlimit(3000)
def F (n):
    if n == 1:
         return 1
    if n > 1:
        return n + 2 + F(n-1)
print(F(2028) + F(2022))