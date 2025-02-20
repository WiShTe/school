f = open("data/3.txt")
cnt = 0
for s in f:
    s = s.split()
    if int(s[0]) - int(s[1]) == int(s[1]) - int(s[2]):
        cnt += 1
print(cnt)