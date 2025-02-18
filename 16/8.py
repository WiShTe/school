def F(n):
    if n < 3:
        return 3
    elif n >= 3:
        return 2 * n + 5 + F(n - 2)
print(F(3027))
