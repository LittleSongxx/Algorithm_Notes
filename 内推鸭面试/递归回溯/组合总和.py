n, target = map(int, input().split())
a = list(map(int, input().split()))

res = []
path = []
def dfs(start, remain):
    # 正好凑齐
    if remain == 0:
        res.append(path[:])
        return

    # 凑过头了
    if remain < 0:
        return

    # 从start开始选
    for i in range(start, n):
        num = a[i]
        path.append(num)
        dfs(i, remain - num) # 可以重复选，所以传i而不是i+1
        path.pop()

dfs(0, target)

for enum in res:
    print(*enum)