n, p = map(int, input().split())
a = list(map(int, input().split()))

# 构造差分数组
d = [0] * n
d[0] = a[0]
for i in range(1, n):
    d[i] = a[i] - a[i - 1]

# 处理每次区间加法
for _ in range(p):
    x, y, z = map(int, input().split())
    l = x - 1
    r = y - 1

    d[l] += z
    if r + 1 < n:
        d[r + 1] -= z

# 前缀和还原最终成绩，并求最小值
cur = 0
ans = float("inf")

for i in range(n):
    cur += d[i]
    if cur < ans:
        ans = cur

print(ans)
