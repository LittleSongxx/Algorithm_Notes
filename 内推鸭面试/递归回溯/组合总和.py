n, target = map(int, input().split())
a = list(map(int, input().split()))

res = []
path = []
def dfs(x):
    if x == 0:
        res.append(path[:])
        return
    for i in range(n):
        path.append(a[i])
        dfs(target - a[i])
        path.pop()

for i in res:
    print(*i)