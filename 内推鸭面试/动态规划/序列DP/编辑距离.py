word1 = input().strip()
word2 = input().strip()

m = len(word1)
n = len(word2)

# dp[i][j] 表示 word1 的前 i 个字符变成 word2 的前 j 个字符需要的最少操作数
dp = [[0] * (n + 1) for _ in range(m + 1)]

# 初始化状态
# word1 前 i 个字符变成空字符串，需要删除 i 次
for i in range(1, m + 1):
    dp[i][0] = i

# 空字符串变成 word2 前 j 个字符，需要插入 j 次
for j in range(1, n + 1):
    dp[0][j] = j

for i in range(1, m + 1):
    for j in range(1, n + 1):
        # 如果最后一个字符不同，则无需操作，最少操作书不变
        if word1[i - 1] == word2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]

        else:
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # 删除
                dp[i][j - 1] + 1,  # 插入
                dp[i - 1][j - 1] + 1  # 替换
            )

print(dp[m][n])
