n = int(input())
intervals = []
for _ in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

# 按左端点排序
intervals.sort(key=lambda x: x[0])

res = []
for l, r in intervals:
    # 如果结果为空，或者当前区间和最后一个区间不重叠
    if not res or l > res[-1][1]:  # res[-1][1]表示结果集中最后一个区间的右端点
        res.append([l, r])
    else:
        res[-1][1] = max(res[-1][1], r)  # 更新右端点

for l, r in res:
    print(l, r)
