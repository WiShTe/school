string = "8" * 9 + "5" * 12
while "555" in string or "888" in string:
    while "555" in string:
        string = string.replace("555", "8", 1)
    while "888" in string:
        string = string.replace("888", "5", 1)
print(string)