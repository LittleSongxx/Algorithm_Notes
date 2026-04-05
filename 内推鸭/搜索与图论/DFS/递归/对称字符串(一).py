def dfs(n, k):  # 递归第n层第k个字符
    if n == 1:  # 记根节点为1（R）
        return 0
    if k % 2 == 0:  # 左孩子，和父节点颜色相反
        return 1 - dfs(n - 1, k // 2)  # 父结点在第 n-1 层的第 k//2 个位置
    else:  # 右孩子，和父节点颜色相同
        return dfs(n - 1, k // 2)


T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    print("red" if dfs(n, k) == 0 else "blue")
