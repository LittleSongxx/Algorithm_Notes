from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = [0] * n  # 用于临时存储当前正在构建的排列

        def dfs(i, s):  # i:当前处理的位置索引   s:剩余可用的数集合
            if i == n:  # 已构建完一个完整排列
                ans.append(path.copy())  # 当后续修改path时，不会影响ans
                return
            for x in s:  # 遍历剩余数字集合 s 中的每个数字 x
                path[i] = x
                dfs(i + 1, s - {x})  # 递归调用 dfs 处理下一个位置 i+1，并从剩余集合中移除 x

        dfs(0, set(nums))
        return ans

    def permute2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = [0] * n
        on_path = [False] * n # 用于标记 nums 中的每个数字是否已经在当前路径中
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            for j in range(n):
                if not on_path[j]: # nums中第j个元素未被使用
                    path[i] = nums[j]
                    on_path[j] = True
                    dfs(i + 1)
                    on_path[j] = False # 恢复现场
        dfs(0)
        return ans

# 示例用法
if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([1, 2, 3]))
    print(sol.permute2([1, 2, 3]))
