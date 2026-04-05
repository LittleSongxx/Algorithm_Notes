from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)  # 统计入度

for _ in range(m):
    x, y = map(int, input().split())  # x y 表示 x 号摄像头能监视 y 号位置

    # 题目说的是“不被其他摄像头监视”
    # 如果 x == y，自己监视自己不影响能不能砸，直接忽略
    if x == y:
        continue

    g[x].append(y)  # 有向边x -> y
    indeg[y] += 1  # y入度加1

q = deque()

# 先统计所有入度为0的结点，即拓扑排序的起点
for i in range(1, n + 1):
    if indeg[i] == 0:
        q.append(i)

cnt = 0

while q:
    cur = q.popleft()
    cnt += 1
    for y in g[cur]:  # 遍历cur节点所在的邻接表，即所有被他指向的节点
        indeg[y] -= 1  # 所有被x指向的结点入度减1
        if indeg[y] == 0:  # 删掉cur这个入度后入度为0
            q.append(y)

# 删掉了全部节点
if cnt == n:
    print("YES")
else:
    print(cnt)
