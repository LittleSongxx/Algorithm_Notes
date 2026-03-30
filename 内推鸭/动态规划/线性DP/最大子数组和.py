from collections import deque

n = int(input())
a = list(map(int, input().split()))

dp = [0] * n  # 以第 i 个数结尾的连续非空子段的最大和
dp[0] = a[0]

for i in range(1, n):
    dp[i] = max(a[i], dp[i - 1] + a[i])  # 对于第i个位置，可以选择从自己开始或接在前面字段的后面

print(max(dp))