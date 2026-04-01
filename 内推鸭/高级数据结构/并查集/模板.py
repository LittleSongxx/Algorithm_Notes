n, m = map(int, input().split())

# parent[i] 表示 i 的父节点
# 一开始每个元素的父节点都是自己
parent = list(range(n + 1))


def find(x):
    # 找到 x 所在集合的根节点
    if parent[x] != x:  # 当x是自己的祖先时即找到
        # 路径压缩：让查找过的点直接连到根节点
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    # 合并 x 和 y 所在的集合
    root_x = find(x)
    root_y = find(y)

    # 如果根节点不同，说明原本不在一个集合里
    if root_x != root_y:
        parent[root_y] = root_x


ans = []

for _ in range(m):
    z, x, y = map(int, input().split())

    if z == 1:
        # 操作 1：合并 x 和 y
        union(x, y)
    else:
        # 操作 2：查询 x 和 y 是否在同一个集合
        if find(x) == find(y):
            ans.append("Y")
        else:
            ans.append("N")

# 按行输出所有查询结果
print("\n".join(ans))
