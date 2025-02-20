f = open("data/2.txt")
s = f.readline()


def koren(n):
    return int(n) ** 0.5 * 4


print(sum(list(map(koren, s.split()))))
