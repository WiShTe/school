f = open("data/2.txt")
s = f.readline()
def squere(n):
    return int(n) ** 2
print(sum(list(map(squere, s.split()))))