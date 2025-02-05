#145*51?2
for x in range(34, 10**9+1, 34):
    if str(x)[0:3] == "145" and str(x)[-1] == "2" and str(x)[-4:-2] == "51":
        print(str(x)+str(x//34))