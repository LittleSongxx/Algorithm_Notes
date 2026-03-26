from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len = max(map(len, wordDict))  # 用于限制下面 j 的循环次数
        words = set(wordDict)  # 便于快速判断 s[j:i] in words，因为 set（集合）的查找时间复杂度是 O(1)，而 list（列表）的查找时间复杂度是 O(n)

        def dfs(i):
            if i == 0:
                return True
            for j in range(i - 1, max(i - 1 - max_len, -1), -1): # 从i-1向前遍历最多max_len个位置
                if s[j:i] in words and dfs(j):
                    return True
            return False

        return dfs(len(s))
