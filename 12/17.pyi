for i in range(4, 10000):
    n = "3" + "4" * i
    while "34" in n or "4444" in n or "6644" in n:
        if "34" in n:
            n = n.replace("34", "66", 1)
        if "4444" in n:
            n = n.replace("4444", "2", 1)
        if "6644" in n:
            n = n.replace("6644", "43", 1)
    f = 0
    for j in n:
        f += int(j)
    if f == 104:
        print(i)

