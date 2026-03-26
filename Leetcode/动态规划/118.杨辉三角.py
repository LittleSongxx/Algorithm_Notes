from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1] * (i + 1) for i in range(numRows)]  # 创建一个二维数组，行数为numRows，列数为i+1，每个元素初始化为1
        for i in range(2, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]  # 每个元素等于上一行的左上角和右上角的和
        return ans


if __name__ == "__main__":
    print(Solution().generate(5))
