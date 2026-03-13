from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        '''
            以逗号放在什么位置的视角来考虑
                i：第i个字符后放不放逗号
                start：当前回文子串的起始位置
        '''

        def dfs(i, start):
            if i == n:  # 遍历完全部字符
                ans.append(path.copy())
                return

            # i和i+1之间不放逗号
            if i < n - 1:
                dfs(i + 1, start)

            # i和i+1之间放逗号
            t = s[start:i + 1]
            if t == t[::-1]:  # 是否回文
                path.append(t)
                dfs(i + 1, i + 1)  # start = i + 1,表示下一个子串从i+1位置开始，即在当前回文串基础上看再往后追加字符还是不是回文串
                path.pop()  # 恢复现场

        dfs(0, 0)
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = "leetcode"
    print(solution.partition(s))
