from cmath import inf
from functools import cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        @cache
        def dfs(i, amt):
            if i < 0:
                return 0 if amt == 0 else inf
            if amt < coins[i]:  # 第i种物品的价值已经超过了需要的总amount，直接转为凑第i-1种物品
                return dfs(i - 1, amt)
            return min(dfs(i - 1, amt),  # 不选第i种物品
                       dfs(i, amt - coins[i]) + 1)  # 选第i种物品，由于选了第i个所以+1

        ans = dfs(n - 1, amount)
        return ans if ans < inf else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(Solution().coinChange(coins, amount))
