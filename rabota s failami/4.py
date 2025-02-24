f = open("data/4.txt")
a = []
pari = []
for s in f:
    a.append(int(s))
for i in range(len(a)-1):
    if str(a[i]**0.5)[-1] == "0" or str(a[i+1]**0.5)[-1] == "0":
        pari.append(a[i] + a[i+1])
print(f'{len(pari)}{max(pari)}')