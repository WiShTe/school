
for i in "0123456789ABCDEFGH":
    if (int(f'AB5{i}3', 18) + int(f'EF{i}13', 18)) %  17 == 0:
        print((int(f'AB5{i}3', 18) + int(f'EF{i}13', 18)) //  17)