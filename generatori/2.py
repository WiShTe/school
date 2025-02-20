fib = [0,1]
for _ in range(10):
    fib.append(sum(fib[-2:]))
print(fib)