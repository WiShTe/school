string = "7" + "32" * 55
while "7" in string or "32" in string:
    if "7" in string:
        string = string.replace("7", "33", 1)
    else:
        if "32" in string:
            string = string.replace("32", "21", 1)
string = string.replace("1", "3")
s_troek = 0
s_dvoek = 0
for x in string:
    if x == "3":
        s_troek += 3
    else:
        s_dvoek += 2
print(abs(s_dvoek-s_troek))