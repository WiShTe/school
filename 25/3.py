#133*23?1
for x in range (669, 10**9 + 1, 669):
    if str(x)[:3] == "133" and str(x)[-1] == "1" and str(x)[-4:-2] == "23":
        print(x, x/669)