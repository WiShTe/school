string = "5"*72
while "333" in string or "555" in string:
    if "555" in string:
        string = string.replace("555","3", 1)
    else:
        string = string.replace("333","5", 1)
print(string)