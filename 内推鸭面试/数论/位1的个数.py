n = int(input())

res = 0
for i in range(32):
    if (n >> i) & 1:
        res += 1
print(res)