from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i, j - 1) + dfs(i - 1, j)

        return dfs(m - 1, n - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 7))
