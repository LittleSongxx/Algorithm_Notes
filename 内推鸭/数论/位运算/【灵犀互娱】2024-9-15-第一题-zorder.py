n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    res = 0

    # 循环 32 次，正好处理 64 位 (x 32次, y 32次)
    for i in range(32):
        # 1. 取出 x 和 y 当前的最低位
        high = x & 1  # 相当于 x % 2
        low = y & 1  # 相当于 y % 2

        # 2. 把它们推到在 res 中该去的位置，并拼接到 res 上
        res |= (low << (2 * i))  # low 放偶数位 (2 * i)
        res |= (high << (2 * i + 1))  # high 放奇数位 (2 * i + 1)

        # 3. x 和 y 右移一位，准备下一次循环提取新的最低位
        x >>= 1  # 相当于你的 x // 2
        y >>= 1  # 相当于你的 y // 2

    print(res)
