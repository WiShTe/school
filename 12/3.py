string = "1" + "8" * 80
while "18" in string or "288" in string or "3888" in string:
    if "18" in string:
        string = string.replace("18", "2", 1)
    if "288" in string:
        string = string.replace("288", "3", 1)
    else:
        string = string.replace("3888", "1", 1)
print(string)