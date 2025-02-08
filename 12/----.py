s = "6" * 60 + "7" * 60 + "8" * 60
while "76" in s or "86" in s or "78" in s:
    if "76" in s:
        s = s.replace("76", "67", 1)
    if "86" in s:
        s = s.replace("86", "68", 1)
    if "78" in s:
        s = s.replace("78", "87", 1)
print(s[33]+s[55]+s[131])