from cmath import inf
from functools import lru_cache
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @lru_cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return inf  # 注意这里要返回数字，不能只return，由于是取min，所以以inf作为错误返回
            if i == 0 and j == 0:
                return grid[0][0]
            return grid[i][j] + min(dfs(i - 1, j), dfs(i, j - 1))

        return dfs(m - 1, n - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
