f = open("data/s.txt")
s = f.readline()


def zad(n):
    return (int(n) % 7) ** 2


print(sum(list(map(zad, s.split()))))
