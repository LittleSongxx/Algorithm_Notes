m, n = map(int, input().split())

# dp[i][j] 表示走到第 i 行第 j 列的方法数
dp = [[0] * n for _ in range(m)]

for i in range(m):
    dp[i][0] = 1

for j in range(n):
    dp[0][j] = 1

'''
    由于本题整个路径中没有障碍
    初始化也可以直接写成 dp = [[1] * n for _ in range(m)]
'''

for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[m - 1][n - 1])
