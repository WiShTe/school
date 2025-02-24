f= open("data/2.txt")
a = []
qvad = []
for s in f:
    a.append(int(s))
for i in range(len(a)-1):
    if a[i] > 500 or a[i+1] > 500:
        qvad.append(a[i]**2 + a[i+1]**2)
print(f'{len(qvad)}{max(qvad)}')