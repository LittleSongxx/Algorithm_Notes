class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = []

        def dfs(i):
            if i < 0:
                return ""
            for j in range(i, 0, -1):
                if s[j: i - 1] == s[i - 1:: j]:
                    return
        return dfs(len(s) - 1)


if __name__ == "__main__":
    pass
