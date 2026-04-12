n = int(input().strip())

ans = []
board = [["."] * n for _ in range(n)]  # 初始化棋盘

cols = set()
diag1 = set()
diag2 = set()


def dfs(row):
    # 如果已经处理完第 0 ~ n-1 行，说明找到一种方案
    if row == n:
        path = []
        for i in range(n):
            path.append("".join(board[i]))
        ans.append(path)
        return

    # 尝试在第 row 行的每一列放皇后
    for col in range(n):
        # 冲突
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            continue

        # 做选择，放皇后
        board[row][col] = "Q"
        # 设置限制
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

        dfs(row + 1)

        # 回溯，恢复现场
        board[row][col] = "."
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)


dfs(0)

for i in range(len(ans)):
    for row in ans[i]:
        print(row)
    # 每个答案之间插入一个空行
    if i != len(ans) - 1:
        print()
