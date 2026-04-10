m, n = map(int, input().split())

board = []

for _ in range(m):
    row = input().split()
    board.append(row)

word = input().strip()


def dfs(i, j, index):
    # 如果 index 已经等于单词长度，说明全部匹配成功
    if index == len(word):
        return True

    # 越界
    if i < 0 or i >= m or j < 0 or j >= n:
        return False

    # 当前递归到的字符不匹配
    if board[i][j] != word[index]:
        return False

    # 记录当前字符，用于后面回溯
    temp = board[i][j]

    # 标记为已经访问过，特殊字符"#"会让后续的 board[i][j] == word[index]判断都为False
    board[i][j] = "#"

    # 往上下左右四个方向搜索下一个字符
    found = (
            dfs(i - 1, j, index + 1) or
            dfs(i + 1, j, index + 1) or
            dfs(i, j - 1, index + 1) or
            dfs(i, j + 1, index + 1)
    )

    # 回溯：恢复当前格子
    board[i][j] = temp

    return found


answer = False

# 从每一个格子出发尝试搜索
for i in range(m):
    for j in range(n):
        if dfs(i, j, 0):
            answer = True
            break
    if answer:
        break

if answer:
    print("true")
else:
    print("false")
