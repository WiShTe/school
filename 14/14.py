print("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[20])
alf = "0123456789ABCDEFGHIJKLMNOPQRST"
for i in "0123456789ABCDEFGHIJKLMNOPQRST":
    if (int(f"39{i}9{i}DE", 30) + int(f"{i}M13F", 30) + int(f"11{i}9", 30)) % 17 == 0:
        print((int(f"39{i}9{i}DE", 30) + int(f"{i}M13F", 30) + int(f"11{i}9", 30)) / 17 )