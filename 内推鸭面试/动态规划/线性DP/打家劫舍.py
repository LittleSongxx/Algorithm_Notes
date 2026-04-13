nums = list(map(int, input().split()))
n = len(nums)
if n == 1:
    print(nums[0])
else:
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    print(dp[n - 1])
