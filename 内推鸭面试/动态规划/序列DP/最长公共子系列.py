text1 = input().strip()
text2 = input().strip()

m = len(text1)
n = len(text2)

# dp[i][j] 表示 text1 前 i 个字符 和 text2 前 j 个字符的最长公共子序列长度
dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if text1[i - 1] == text2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[m][n])
