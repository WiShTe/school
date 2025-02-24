f = open("data/3.txt")
a = []
troiki =[]
for s in f:
    a.append(int(s))
for i in range(len(a)-2):
    if a[i] < 0 or a[i+1] < 0 or a[i+2] < 0:
        troiki.append(a[i] + a[i+1]+a[i+2])
print(f'{len(troiki)}{min(troiki)}')