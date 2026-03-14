from functools import lru_cache  # 或 from functools import cache


class Solution:
    """
       递归法
    """

    def climbStairs(self, n: int) -> int:
        memo = {}

        @lru_cache  # 自动缓存函数的返回值
        def dfs(i):
            # if i in memo:  # 如果已缓存，直接返回
            #     return memo[i]
            if i <= 1:
                return 1
            else:
                return dfs(i - 1) + dfs(i - 2)
            memo[i] = result
            return result

        return dfs(n)

    """
       递推法
    """

    def climbStairs2(self, n: int) -> int:
        f = [0] * (n + 1)
        f[0] = f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]

    """
       空间优化
    """

    def climbStairs3(self, n: int) -> int:
        f0 = f1 = 1
        for _ in range(2, n + 1):
            new_f = f1 + f0
            f0 = f1
            f1 = new_f
        return f1


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(3))
    print(s.climbStairs2(3))
