from itertools import count
s  = 64**13  + 32**6 - 16**2
n = bin(s)
print(n[2:].count("1"))