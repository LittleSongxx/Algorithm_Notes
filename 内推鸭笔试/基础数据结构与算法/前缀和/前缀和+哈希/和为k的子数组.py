from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

pre = [0] * (n + 1)
for i in range(1, n + 1):
    pre[i] = pre[i - 1] + a[i - 1]

cnt = defaultdict(int)
ans = 0

for s in pre:
    ans += cnt[s - k]  # 当前前缀和s减去目标区间和即为剩下所需前缀和
    cnt[s] += 1  # 记录前缀和为s的个数

print(ans)