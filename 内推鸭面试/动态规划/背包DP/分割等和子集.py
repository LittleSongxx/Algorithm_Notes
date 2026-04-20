nums = list(map(int, input().split()))

if sum(nums) % 2 != 0:
    print("false")
else:
    target = sum(nums) // 2
    dp = [0] * (target + 1)  # dp[j] 里的 j 表示的是 和/容量，而这个 j 需要从 0 一直到 target

    # 遍历每一个物品，这题每一个数就是一个物品
    for x in nums:
        # 拿当前遍历到的这个数去更新所有能容纳这个数j对应的最大价值
        for j in range(target, x - 1, -1):
            dp[j] = max(dp[j], dp[j - x] + x)
            # 等价于 dp[j] = d[j] or dp[j - x] 因为这题的重量和价值一样
    print("true" if dp[target] else "false")