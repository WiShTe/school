def F(n):
    if n < 2:
        return n
    else:
        return F(n-1)*(n+5)
print(F(5))