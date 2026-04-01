from math import inf

n = int(input())

intervals = []
mn = inf
mx = 0

for _ in range(n):
    a, b = map(int, input().split())
    intervals.append((a, b))
    mn = min(mn, a)
    mx = max(mx, b)

# 差分数组，开到 mx + 2，保证能访问 b + 1
diff = [0] * (mx + 2)

# 对每个闭区间 [a, b] 做差分
for a, b in intervals:
    diff[a] += 1
    diff[b + 1] -= 1

ans = 0
cur = 0

# 只需要统计从最早开始时间到最晚结束时间
for t in range(mn, mx + 1):
    cur += diff[t]  # 当前时刻正在监视的考场数

    if cur == 0:
        ans += 1
    elif cur == 1:
        ans += 3
    else:
        ans += 4

print(ans)
