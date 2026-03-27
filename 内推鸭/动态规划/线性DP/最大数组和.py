from math import inf

n = int(input())
a = list(map(int, input().split()))

sum = sum(a)
dp = [sum] * n
curr = 0
for i in range(n):
    if a[i] % 2 == 0:
        dp[i] += max(a[i], a[i] // 2)
    else:
        dp[i] = a[i]