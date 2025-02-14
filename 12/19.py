for i in range(3, 10001):
    n = 0
    s = "7" + "8" * i
    while "788" in s or "988" in s or "798" in s:
        if "788" in s:
            s = s.replace("788", "79", 1)
        if "988" in s:
            s = s.replace("988", "78", 1)
        if "798" in s:
            s = s.replace("798", "98", 1)
    for j in s:
        n += int(j)
    if n == 17:
        print(i)


