import heapq

n = int(input())
m = int(input())
q = list(map(int, input().split()))

heap = []

for i in range(n):
    need = (q[i] + m - 1) // m
    heapq.heappush(heap, (need, i + 1))

ans = []

while heap:
    need, idx = heapq.heappop(heap)
    ans.append(idx)

print(*ans)
