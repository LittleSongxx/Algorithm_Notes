n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    z = []
    res = 0
    while True:
        high = x % 2
        x = x // 2
        low = y % 2
        y = y // 2
        z.append(low)
        z.append(high)
        if len(z) == 64:
            break
    print(z)
    for i in range(len(z)):
        res += z[i] * (pow(2, i))
    print(res)