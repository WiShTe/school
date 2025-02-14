s = 789012 + 678901 - 23456
alf = "0123456789ABCDEFGHIJ"
otv  = ""
while s > 0:
    otv += str(alf[s%20])
    s = s//20
print(otv[::-1])