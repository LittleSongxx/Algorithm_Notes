from collections import deque

n = int(input().strip())
w = list(map(int, input().split()))

# matrix[i][j] = 1 表示：任务 i 依赖任务 j
matrix = [list(map(int, input().split())) for _ in range(n)]

# 建图：如果 i 依赖 j，那么边是 j -> i
graph = [[] for _ in range(n)]
indegree = [0] * n  # 这题是通过邻接矩阵建图的，下标也是从0开始，而不是1号节点2号节点等等，所以不必开n+1对齐

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            graph[j].append(i)
            indegree[i] += 1

# 入度为0的先全部入队
q = deque()
for i in range(n):
    if indegree[i] == 0:
        q.append(i)

processed = 0  # processed: 已经完成的任务数量
ans = 0  # answer: 系统执行所有任务所需的最小内存

while q:
    level_size = len(q)
    level_memory = 0
    for _ in range(level_size):
        cur = q.popleft()
        processed += 1
        # 累加到这一层使用的内存和
        level_memory += w[cur]

        for i in graph[cur]:  # 遍历当前节点所在邻接表
            indegree[i] -= 1  # 由于删了cur，所以被他指的节点入度都减一
            if indegree[i] == 0:
                q.append(i)

    # 统计历史最大的内存需求量
    ans = max(ans, level_memory)

if processed < n:
    print(-1)
else:
    print(ans)
