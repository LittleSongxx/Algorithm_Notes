nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

m = len(nums1)
n = len(nums2)

# dp[i][j] 表示以 nums1[i-1] 和 nums2[j-1] 结尾的最长公共子数组长度
dp = [[0] * (n + 1) for _ in range(m + 1)]

ans = 0

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if nums1[i - 1] == nums2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            ans = max(ans, dp[i][j])
        # 由于初始化为0，所以这一步可以不写
        # else:
        #     dp[i][j] = 0
print(ans)
