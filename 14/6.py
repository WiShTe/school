import string

print(string.ascii_uppercase)
alf = "0123456789ABCDEFGH"
for i in range(18):
    if (int(f'AB5{alf[i]}3', 18) + int(f'EF{alf[i]}13', 18)) % 17 == 0:
        print((int(f'AB5{alf[i]}3', 18) + int(f'EF{alf[i]}13', 18)) // 17)
