alf = "0123456789ABCDEF"
for i in range (16):
    if (int(f'D49{alf[i]}1', 16) + int(f'48A3{alf[i]}', 16)) % 14 == 0:
        print((int(f'D49{alf[i]}1', 16) + int(f'48A3{alf[i]}', 16)) / 14)