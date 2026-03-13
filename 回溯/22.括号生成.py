from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2 * n
        ans = []
        path = [''] * m

        '''
            考虑括号的匹配性，右括号的数量永远不能超过左括号的数量
                1. 当左括号数量小于n时，可以无脑放一个左括号，递归dfs(left + 1, right)
                2. 当右括号数量小于左括号数量时，才可以放一个右括号，递归dfs(left, right + 1)
                3. 当右括号数量等于n时，说明已经放满了，可以将当前路径加入答案中
        '''

        def dfs(left, right) -> None:
            if right == n:
                ans.append(''.join(path))
                return
            if left < n:
                # left + right表示当前已经生成的括号数，而path[left + right]刚好可以覆盖最后一次生成的括号，实现回溯
                path[left + right] = '('
                dfs(left + 1, right)
            if right < left:
                path[left + right] = ')'
                dfs(left, right + 1)

        dfs(0, 0)
        return ans


if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(n))
