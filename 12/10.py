s = "1" * 60 + "2" * 60 + "3" * 60
while "21" in s or "31" in s or "23" in s:
    if "21" in s:
        s = s.replace("21", "12")
    if "31" in s:
        s = s.replace("31", "13")
    if "23" in s:
        s = s.replace("23", "32")
print(s[20]+s[100]+s[140])
