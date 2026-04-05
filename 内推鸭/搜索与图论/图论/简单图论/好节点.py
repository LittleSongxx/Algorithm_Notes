n, k = map(int, input().split())

# deg[i] 表示第 i 个点连接了多少条边
deg = [0] * (n + 1)  # 开n+1个位置单纯为了让后续输入结点下标和顺序一样对应

# 读入 n-1 条边，统计每个点的度数
for _ in range(n - 1):
    a, b = map(int, input().split())
    # 无向边，直接统计每个输入结点的度
    deg[a] += 1
    deg[b] += 1

ans = 0

# 根节点 1 的子节点个数就是它的度数
if deg[1] == k:
    ans += 1

# 其他节点的子节点个数 = 度数 - 1
for i in range(2, n + 1):
    if deg[i] - 1 == k:
        ans += 1

print(ans)
