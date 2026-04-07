n = int(input())
deg = [0] * (n + 1)

# 只需要统计每个点的度数
for _ in range(n - 1):
    u, v = map(int, input().split())
    deg[u] += 1
    deg[v] += 1

ans = 0

for i in range(1, n + 1):
    ans += deg[i] * deg[i + 1] // 2

print(ans)
