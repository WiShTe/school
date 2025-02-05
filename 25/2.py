#64*32?2
for x in range(339, 10**8+1, 339):
    if str(x)[0:2] == "64" and str(x)[-1] == "2" and str(x)[-4:-2] == "32" and x%339 == 0:
        print(x, x/339)