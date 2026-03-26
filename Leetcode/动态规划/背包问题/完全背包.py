from functools import cache, lru_cache
from typing import List


class Solution:
    """
      完全背包问题：
      - 有n件物品，每件物品有重量w[i]和价值v[i]
      - 背包容量为capacity
      - 每件物品可以重复选
      - 求不超过背包容量的最大价值
    """

    def complete_knapsack_recursive(self, capacity: int, w: List[int], v: List[int]) -> int:
        """
        递归法
        时间复杂度: O(n * capacity)
        空间复杂度: O(n * capacity)
        """
        n = len(w)

        @lru_cache(maxsize=None)
        def dfs(i: int, cap: int) -> int:
            if i < 0:
                return 0

            # 不选第 i 个物品
            ans = dfs(i - 1, cap)

            # 选第 i 个物品后，仍然可以继续选第 i 个
            if cap >= w[i]:
                ans = max(ans,  # 不选
                          dfs(i, cap - w[i]) + v[i])  # 选，还可以继续选第i个

            return ans

        return dfs(n - 1, capacity)
