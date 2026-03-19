from typing import List

"""
   定义 dp[i] 为：以第 i 个元素结尾的，具有最大和的连续子数组的和
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]  # Base case: 第一个元素结尾的最大和就是它自己
        max_sum = dp[0]  # 用于记录全局最大值

        for i in range(1, n):
            # 状态转移：要么和前面连起来，要么自己单干
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            # 更新全局最大值
            max_sum = max(max_sum, dp[i])

        return max_sum

    '''
        计算 dp[i] 的时候，其实我们只需要用到 dp[i-1]，再往前的数据（比如 dp[i-2]）我们根本用不上了。
        既然如此，我们完全不需要保留整个 dp 数组,我们只需要一个变量 pre 来记录“上一个元素结尾的最大和”就可以了。
    '''
    def maxSubArray_DP_v2(nums):
        if not nums: return 0

        pre = nums[0]    # 相当于 dp[i-1]
        max_sum = pre    # 全局最大值

        for i in range(1, len(nums)):
            # pre 更新为以当前元素结尾的最大和
            pre = max(pre + nums[i], nums[i])
            # 随时记录出现过的最大值
            max_sum = max(max_sum, pre)

        return max_sum


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
