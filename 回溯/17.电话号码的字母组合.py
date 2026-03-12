from typing import List

MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = [''] * n

        def dfs(i):
            if i == n:
                ans.append(''.join(path))
                return
            # 遍历digits[i] 对应的字母集合，例如digits[i] = '2'，对应的字母集合为 'abc'
            for c in MAPPING[int(digits[i])]:
                path[i] = c
                dfs(i + 1)
                # 由于后续赋值会覆盖当前值，所以隐式的恢复现场，实现了回溯

        dfs(0)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
