for i in "123456789ABCDEFGHIJ":
    for j in "0123456789ABCDEFGHIJ":
        d = int(f'32{i}333{j}6', 20)
        if d  % 14 == 0:
            print(int(f'{i}{j}', 20))