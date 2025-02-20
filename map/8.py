f = open("data/4.txt")
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    if a[0] % 3 + a[1] % 3 + a[2] % 3 == 5:
        cnt += 1
print(cnt)