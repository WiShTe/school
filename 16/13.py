from sys import setrecursionlimit
setrecursionlimit(3000)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n-1)
def G(n):
    if n == 1:
        return 1
    if n > 1:
        return 3 * n * G(n-1)
print((G(2025)+G(2024))/G(2023)-(F(2024)+F(2023))/F(2022))
