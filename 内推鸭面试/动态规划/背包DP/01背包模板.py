n, W = map(int, input().split())

# 先把所有物品数据读入
# 为了让物品编号从 1 开始，先放一个占位 0
weights = [0]
values = [0]

for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# dp[i][j] 表示：
# 只考虑前 i 个物品，背包容量为 j 时，可以获得的最大价值
dp = [[0] * (W + 1) for _ in range(n + 1)]

# 枚举物品
for i in range(1, n + 1):
    weight = weights[i]
    value = values[i]

    # 枚举背包容量
    for j in range(W + 1):
        # 情况 1：不选第 i 个物品
        dp[i][j] = dp[i - 1][j]

        # 情况 2：如果容量足够，可以选第 i 个物品
        if j >= weights[i]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - weights[i]] + values[i])

# 输出只考虑前 n 个物品，容量为 W 时的最大价值
print(dp[n][W])