n = int(input())

res = []
path = []


def dfs(left, right):
    # left 表示已经用了几个左括号
    # right 表示已经用了几个右括号

    # 如果已经放了 2 * n 个括号，说明得到一个完整答案
    if len(path) == 2 * n:
        res.append("".join(path))
        return

    # 左括号还没用完，就可以继续加左括号
    if left < n:
        path.append("(")  # 做选择
        dfs(left + 1, right)  # 继续递归
        path.pop()  # 撤销选择，这一步就是回溯

    # 右括号数量必须小于左括号数量，才能加右括号
    if right < left:
        path.append(")")  # 做选择
        dfs(left, right + 1)  # 继续递归
        path.pop()  # 撤销选择，这一步就是回溯


dfs(0, 0)

for s in res:
    print(s)
