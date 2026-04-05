n = int(input())
deg = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    deg[u] += 1
    deg[v] += 1

ans = 0
for i in range(1, n + 1):
    if deg[i] == 2:
        ans += 1

print(ans)
