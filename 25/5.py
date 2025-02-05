#123*578
for x in range(31, 10**8+1, 31):
    if str(x)[0:3] == "123" and str(x)[-3:]=="578":
        print(str(x)+str(x//31))