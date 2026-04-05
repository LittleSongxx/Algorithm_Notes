s = input()
n = len(s)
res = []


def dfs(u, t):
    if u == n:
        if t:
            res.append(t)
        return
    dfs(u + 1, t)  # 不选择第u个字符
    dfs(u + 1, t + s[u])  # 选择第u个字符


dfs(0, "")
res.sort()  # 对于所有的子序列，按照字典序升序排列
for str in res:
    print(str)
