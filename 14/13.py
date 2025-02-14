print("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[17])
for i in "0123456789ABCDEFGHIJKLMNOPQ":
    if (int(f'{i}1{i}2{i}3{i}4{i}5', 27) + int(f'20{i}204',27) + int(f'20{i}20', 27)) % 25 == 0:
        print((int(f'{i}1{i}2{i}3{i}4{i}5', 27) + int(f'20{i}204',27) + int(f'20{i}20', 27)) / 25)


