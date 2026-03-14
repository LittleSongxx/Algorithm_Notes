from typing import List
from functools import lru_cache


class Solution:
    """
      01背包问题：
      - 有n件物品，每件物品有重量w[i]和价值v[i]
      - 背包容量为capacity
      - 每件物品只能选0或1次
      - 求不超过背包容量的最大价值
    """

    def zero_one_knapsack_recursive(self, capacity: int, w: List[int], v: List[int]) -> int:
        """
        递归法（无优化，存在大量重复计算）
        时间复杂度: O(2^n)
        空间复杂度: O(n)
        """
        n = len(w)

        @lru_cache(maxsize=None)
        def dfs(i, cap):
            if i < 0:
                return 0
            # 01背包问题由于每个物品最多选一次，所以不论选不选都是递归到i-1
            if cap < w[i]:  # 装不下第i个物品
                return dfs(i - 1, cap)  # 直接递归下一个
            return max(dfs(i - 1, cap),  # 不选
                       dfs(i - 1, cap - w[i]) + v[i])  # 选，容量减少，value增加

        return dfs(n - 1, capacity)

    def zero_one_knapsack_2d(self, capacity: int, w: List[int], v: List[int]) -> int:
        """
        递推法（二维数组）
        dfs[i][j] 表示考虑前i件物品，背包容量为j时的最大价值
        时间复杂度: O(n * capacity)
        空间复杂度: O(n * capacity)
        """
        n = len(w)
        dfs = [[0] * (capacity + 1) for _ in range(n)]  # n行capacity+1列的二维数组

        for j in range(w[0], capacity + 1):
            dfs[0][j] = v[0]

        for i in range(1, n): # 遍历每件物品
            for j in range(capacity + 1):  # 遍历每个可能的容量
                if j < w[i]: # 容量不足
                    dfs[i][j] = dfs[i - 1][j]
                else:
                    dfs[i][j] = max(dfs[i - 1][j], dfs[i - 1][j - w[i]] + v[i])

        return dfs[n - 1][capacity]

    def zero_one_knapsack_1d(self, capacity: int, w: List[int], v: List[int]) -> int:
        """
        递推法（一维数组优化）
        dfs[j] 表示背包容量为j时的最大价值
        关键：倒序遍历容量，避免物品重复选择
        时间复杂度: O(n * capacity)
        空间复杂度: O(capacity)
        """
        n = len(w)
        dfs = [0] * (capacity + 1)

        for i in range(n):
            for j in range(capacity, w[i] - 1, -1):
                dfs[j] = max(dfs[j], dfs[j - w[i]] + v[i])

        return dfs[capacity]


if __name__ == '__main__':
    s = Solution()
