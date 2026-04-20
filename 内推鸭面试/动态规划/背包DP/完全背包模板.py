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

    for j in range(w, W + 1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[W])
