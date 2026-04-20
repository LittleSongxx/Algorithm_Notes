from cmath import inf

n = int(input())

ans = 0
dp = [inf] * (n + 1)  # dp[j]表示凑出和为 j 时，最少需要多少个完全平方数
dp[0] = 0

i = 1
# 从1-n中选一个物品
while i * i <= n:
    w = i * i
    # 看假如这个数能否使得恰好凑成j用的个数更多
    for j in range(w, n + 1):
        # 不用当前平方数：dp[j]
        # 用一个当前平方数：dp[j - w] + 1
        dp[j] = min(dp[j], dp[j - w] + 1)
    i += 1

print(dp[n])
