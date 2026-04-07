from collections import deque

# 读入队伍数量 n，比赛结果数量 m
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

indegree = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

count = 0
many = False

while q:
    if len(q) > 1:
        many = True
    cur = q.popleft()
    count += 1
    for i in graph[cur]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if count < n:
    print("No Results")
elif many:
    print("Many Sorted Results")
else:
    print("Only One Sorted Results")
