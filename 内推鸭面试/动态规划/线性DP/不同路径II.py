m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

dp = [[0] * n for _ in range(m)]

# 起点是障碍物，直接无路可走
if grid[0][0] == 1:
    print(0)
else:
    dp[0][0] = 1

    # 初始化第一列
    for i in range(1, m):
        # 当前子目标点不是障碍物且上一步可达当前位置
        if grid[i][0] == 0 and dp[i - 1][0] != 0:
            dp[i][0] = 1

    # 初始化第一行
    for j in range(1, n):
        if grid[0][j] == 0 and dp[0][j - 1] != 0:
            dp[0][j] = 1

    # 状态转移
    for i in range(1, m):
        for j in range(1, n):
            # 障碍物
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    print(dp[m - 1][n - 1])
