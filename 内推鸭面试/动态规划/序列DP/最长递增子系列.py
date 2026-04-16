nums = list(map(int, input().split()))
n = len(nums)

# dp[i] 表示以 nums[i] 结尾的最长递增子序列长度
dp = [1] * n

for i in range(n):
    # 看能接在谁后面
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
