s = input().strip()
target = "bengtie"
n = len(s)

path = []


def dfs(index, pre):
    if index == n:
        new_string = ''.join(path)
        return 1 if target in new_string else 0

    total = 0

    path.append(s[index])
    total += dfs(index + 1, False)
    path.pop()  # 回溯

    if not pre:
        total += dfs(index + 1, True)

    return total


print(dfs(0, False))
