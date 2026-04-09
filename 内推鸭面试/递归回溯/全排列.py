nums = list(map(int, input().split()))

res = []  # 存放所有结果
path = []  # 当前正在构造的排列
used = [False] * len(nums)  # 记录每个数字是否已经用过
n = len(nums)


def dfs():
    if len(path) == n:
        res.append(path[:])  # path[:] 是拷贝一份，避免后面修改影响结果
        return

    for i in range(n):
        if used[i]:
            continue
        # 做选择
        path.append(nums[i])
        used[i] = True
        # 进入下一层递归
        dfs()
        # 撤销选择
        path.pop()
        used[i] = False


dfs()

for i in res:
    print(*i)
