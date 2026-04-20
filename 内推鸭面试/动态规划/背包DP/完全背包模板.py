n, W = map(int, input().split())

weights = []
values = []

for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp = [0] * (W + 1)

for i in range(n):
    w = weights[i]
    v = values[i]

    # 核心差别只在这个for循环，正向循环会有重复，符合完全背包定义
    for j in range(w, W + 1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[W])
