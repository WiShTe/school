for i in range(4, 10000):
    s = "2" + "5" * i
    while "25" in s or "2222" in s or "2233" in s:
        if "25" in s:
            s = s.replace("25", "33", 1)
        if "2222" in s:
            s = s.replace("2222", "5", 1)
        if "2233" in s:
            s = s.replace("2233", "52", 1)
    f = 0
    for j in s:
        f += int(j)
    if int(f ** 0.5) == float(f ** 0.5):
        print(i)

