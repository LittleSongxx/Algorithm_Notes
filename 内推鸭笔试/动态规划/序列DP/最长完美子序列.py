s, k = input().split()
k = int(k)

dp = [0] * 26

for ch in s:
    x = ord(ch) - ord('a')

    left = max(0, x - k)
    right = min(25, x + k)

    best = 1

    for j in range(left, right + 1):
        best = max(best, dp[j] + 1)

    dp[x] = max(dp[x], best)

print(max(dp))
