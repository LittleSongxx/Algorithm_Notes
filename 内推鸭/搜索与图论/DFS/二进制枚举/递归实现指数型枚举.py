n = int(input())

path = []
ans = []


def dfs(i):
    if not path:
        print()
    else:
        print(*path)

    for num in range(i, n + 1):
        path.append(num)
        dfs(num + 1)
        path.pop()


dfs(1)
