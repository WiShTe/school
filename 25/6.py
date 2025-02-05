#45??93*3
from fnmatch import *
for x in range(443, 10**9 + 1, 443):
    flag = 0
    if fnmatch(str(x), '45??93*3'):
        if x%12 != 0:
            for i in str(x):
                if i == "6":
                    flag += 1
        if flag == 2:
            print(x)