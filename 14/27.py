for c in range(37):
    for d in range(37):
        num = 4 * 37**6 + 5 * 37 ** 5 + c * 37 ** 4 + 7 * 37 ** 3 + 3 * 37 ** 2 + d * 37 ** 1 + 9 * 37 ** 0
        if num % 15 == 0 :
            print(c * 37 ** 1+d * 37 ** 0)