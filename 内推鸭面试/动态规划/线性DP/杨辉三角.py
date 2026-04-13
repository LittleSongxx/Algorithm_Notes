numRows = int(input())

dp = []

for i in range(numRows):
    # 先把这一行都初始化成 1
    row = [1] * (i + 1)

    # 计算中间位置
    for j in range(1, i):
        row[j] = dp[i - 1][j - 1] + dp[i - 1][j]

    dp.append(row)

for row in dp:
    print(*row)