import heapq

n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())

    edges[a].append(b)
    indeg[b] += 1

heap = []

for i in range(1, n + 1):
    if indeg[i] == 0:
        heapq.heappush(heap, i)

ans = []

while heap:
    cur = heapq.heappop(heap)
    ans.append(cur)
    for i in edges[cur]:
        indeg[i] -= 1
        if indeg[i] == 0:
            heapq.heappush(heap, i)

print(*ans)
