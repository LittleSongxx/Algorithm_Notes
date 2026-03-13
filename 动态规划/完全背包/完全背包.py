from functools import cache
from typing import List


class Solution:


    def full_knapsack(self, capacity: int, w: List[int], v: List[int]) -> int:
        n = len(w)

        @cache
        def dp(i, cap):
            if i < 0:
                return 0 if cap == 0 else 0
            if cap < w[i]: # 第i种物品的价值已经超过了需要的总amount，直接转为凑第i-1种物品
                return dp(i - 1, cap)
            return min(dp(i - 1, cap), dp(i, cap - w[i]) + 1)
        return dp(n, capacity)

    """
       递推法
    """