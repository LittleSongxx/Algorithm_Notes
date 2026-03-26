from functools import lru_cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total / 2

        @lru_cache
        def dfs(i, res):
            if i < 0:
                return res == 0  # 所有数字遍历完时必须和为一半才返回True
            if res < nums[i]:  # 当前数超过了剩余所需大小
                return dfs(i - 1, res)  # 只能不选
            return dfs(i - 1, res) or dfs(i - 1, res - nums[i])

        return dfs(n - 1, half)


if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1, 2, 3, 5]))
