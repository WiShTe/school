string = "2006" * 298
while "200" in string or "666" in string:
    string = string.replace("200", "66")
    string = string.replace("666", "66")
print(string)