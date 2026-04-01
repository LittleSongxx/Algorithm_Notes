from collections import defaultdict

N, K = map(int, input().split())
A = [0] * N
for i in range(N):
    A[i] = int(input())

pre = [0] * (N + 1)
for i in range(1, N + 1):
    pre[i] = pre[i - 1] + A[i - 1]

cnt = defaultdict(int)
ans = 0

# 只要两个前缀和除以 K 的余数相同，它们之间这一段的和就是 K 的倍数。
for s in pre:
    r = s % K
    ans += cnt[r]
    cnt[r] += 1  # 记录余数为r的个数

print(ans)