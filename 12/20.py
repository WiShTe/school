for i in range(4,10001):
    s = "2" + "9" * i
    n = 0
    while "29" in s or "399" in s or "99" in s:
        if "29" in s:
            s = s.replace("29", "9", 1)
        if "399" in s:
            s = s.replace("399", "92", 1)
        if "99" in s:
            s = s.replace("99", "3", 1)
    for j in s:
        if int(j) % 2 != 0:
            n += 1
    if n == 10:
        print(i)
        break