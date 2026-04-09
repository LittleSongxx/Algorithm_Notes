nums = list(map(int, input().split()))
n = len(nums)

path = []
res = []


def dfs(start):
    if path:
        res.append(path[:])

    for i in range(start, n):
        path.append(nums[i])
        dfs(i + 1)  # 只能选后面的数
        path.pop()


dfs(0)

for i in res:
    print(*i)
