s = ">" + 22 * "6" + 14 * "7" + 16 * "8"
o = 0
while ">6" in s or ">7" in s or ">8" in s:
    if ">6" in s:
        s = s.replace(">6", "77>", 1)
    if ">7" in s:
        s = s.replace(">7", "7>", 1)
    if ">8" in s:
        s = s.replace(">8", "6>", 1)
for i in s:
    if i != ">":
        o += int(i)
print(o)
