f = open("data/4.txt")
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    if sum(a) / 3 < 100:
        cnt += 1
print(cnt)