from math import inf

coins = list(map(int, input().split()))
amount = int(input())

dp = [inf] * (amount + 1)
dp[0] = 0

for w in coins:
    for j in range(w, amount + 1):
        dp[j] = min(dp[j], dp[j - w] + 1)

if dp[amount] == inf:
    print(-1)
else:
    print(dp[amount])