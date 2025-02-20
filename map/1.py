def squere(n):
    return int(n) ** 2
f = open("data/s.txt")
s = f.readline()
print(list(map(squere, s.split())))