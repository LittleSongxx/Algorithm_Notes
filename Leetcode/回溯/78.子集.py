from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []

        def dfs(i):  # i：当前处理的元素索引（nums[i]）
            if i == n:
                ans.append(path.copy()) # 防止修改了后续的ans
                return
            # 不选当前元素nums[i]
            dfs(i + 1)  # 直接递归调用 dfs(i + 1)，处理下一个元素

            # 选 nums[i]
            path.append(nums[i])
            dfs(i + 1)
            path.pop()  # 恢复现场

        dfs(0)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
