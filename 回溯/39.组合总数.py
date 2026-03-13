from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        n = len(candidates)

        def dfs(i, left):
            if left == 0:
                ans.append(path.copy())
                return

            if i == n or left < 0:
                return

            dfs(i + 1, left)  # 不选，保持剩余需要的数left不变，递归下一个数i+1
            path.append(candidates[i])

            dfs(i, left - candidates[i])  # 选，还需要left - candidates[i]
            path.pop()  # 恢复现场

        dfs(0, target)
        return ans

if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))