f = open("data/3.txt")
cnt = 0
for s in f:
    s = s.split()
    x = int(s[0])
    y = int(s[1])
    z = int(s[2])
    if x < y +z and y < z + x and z < x + y:
        cnt += 1
print(cnt)