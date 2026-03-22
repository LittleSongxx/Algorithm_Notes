from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # 记录当前能到达的最远距离（下标）
        max_reach = 0
        for i in range(n):
            # 如果当前下标已经超过了能到达的最远距离，说明卡死了
            if i > max_reach:
                return False
            # 贪心更新：比较“之前能到达的最远距离”和“从当前位置起跳能到达的最远距离”
            max_reach = max(max_reach, i + nums[i])
            # 提前优化：如果最远可达范围已经盖住了终点，直接返回 True
            if max_reach >= n - 1:
                return True
        return True

if __name__ == "__main__":
    pass
