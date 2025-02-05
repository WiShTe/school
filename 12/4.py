string = "2" * 1 + "5" * 81
while "25" in string or "355" in string or "4555" in string:
    if "25"  in string:
        string = string.replace("25", "4", 1)
    if "355" in string:
        string = string.replace("355", "2", 1)
    if "4555" in string:
        string = string.replace("4555", "3", 1)
print(string)