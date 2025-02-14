for i in "0123456789ABCDEFGHIJ":
    if (int(f'13{i}CF', 20) + int(f'47GH{i}', 20)) % 19 == 0:
        print((int(f'13{i}CF', 20) + int(f'47GH{i}', 20)) // 19)