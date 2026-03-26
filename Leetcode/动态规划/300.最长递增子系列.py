from functools import lru_cache
from typing import List


class Solution:
    '''
       相邻相关子序列问题，应该考虑枚举选哪个，而不是像01背包那种相邻无关子序列问题，考虑选或不选
    '''

    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache
        def dfs(i) -> int:  # dfs(i) 表示以 nums[i] 结尾的最长递增子序列的长度
            ans = 0
            for j in range(i):  # 从前往后遍历
                if nums[j] < nums[i]:  # 前一个面的比当前的小，构成递增
                    ans = max(ans, dfs(j))
            return ans + 1  # nums[i]本身可以单独构成长度为1的LIS

        return max(dfs(i) for i in range(len(nums)))  # 枚举每个位置 i 作为结尾
