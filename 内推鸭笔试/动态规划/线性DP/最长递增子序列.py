nums = list(map(int, input().split()))
n = len(nums)

dp = [1] * n  # 以 nums[i] 结尾的最长严格递增子序列长度

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
