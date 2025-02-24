f = open("data/1.txt")
a = []
count = 0
par = []
for s in f:
    a.append(int(s))
for i in range(len(a)-1):
    if a[i] % 8 == 0 and a[i+1] %8 == 0:
        par.append(min(abs(a[i]-a[i+1]), abs(a[i+1]-a[i])))
        count += 1
print(count+min(par))