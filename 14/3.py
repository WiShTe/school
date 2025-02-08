s = 1024**789 +  256**678- 64**567
p = ""
while s > 0:
    p += str(s % 5)
    s = s // 5
print(p.count("4"))