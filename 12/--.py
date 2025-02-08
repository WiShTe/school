s = "1" * 60 + "2" * 60 + "3" * 60
while "12" in s or "32" in s or "31" in s:
    if "12" in s:
        s = s.replace("12", "21", 1)
    if  "32" in s:
        s = s.replace("32", "23", 1)
    if "31" in s:
        s =s.replace("31", "13", 1)
print(s[3], s[119], s[40])