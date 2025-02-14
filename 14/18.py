s = 7777**290  - 777**29 + 77**2 - 7
mn = []
while s > 0:
    mn.append(s%20)
    s = s//20
h = set(mn)
print(len(h))