from functools import lru_cache
@lru_cache()
def F(n):
    if n == 1:
        return 1
    if n >= 2:
       return F(n-1) + 3 * G(n-1) + n
@lru_cache()
def G(n):
    if n == 1:
        return 1
    if n >= 2:
        return 11 * F(n - 1) + G(n - 1) * 2 - n* n
print(F(28)/G(14))