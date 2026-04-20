n, W = map(int, input().split())

weights = []
values = []

for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp = [0] * (W + 1)  # dp[j] 表示：背包容量恰好不超过 j 时，能得到的最大价值。并且容量j从0到W，所有共W+1

# for 每个物品:
#     for 容量从大到小:

for i in range(n):
    # 遍历每一个物品和其对应的重量和价值
    w = weights[i]
    v = values[i]

    # 遍历并更新所有能装下这个物品的容量j对应能取得的最大价值
    # 也就是看新来的这个数i能不能让背包在不超容量的情况下价值更大
    for j in range(W, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[W])
