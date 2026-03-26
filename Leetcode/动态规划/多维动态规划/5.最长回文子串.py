class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # 第一步：预处理字符串，消除奇偶长度的差异
        # 例如: "babad" -> "^#b#a#b#a#d#$"
        T = "^#" + "#".join(s) + "#$"
        n = len(T)

        P = [0] * n  # P[i] 记录以 T[i] 为中心的最长回文半径
        C = 0  # 最右回文边界对应的中心点
        R = 0  # 当前所能到达的最右回文边界

        max_len = 0  # 记录最长回文子串的长度
        center_index = 0  # 记录最长回文子串的中心位置

        # 第二步：核心遍历 (忽略首尾的 ^ 和 $)
        for i in range(1, n - 1):
            # 找 i 关于 C 的对称点 j
            j = 2 * C - i

            # 核心优化：如果 i 在 R 的范围内，利用对称性给出 P[i] 的初始保底值
            if i < R:
                P[i] = min(R - i, P[j])
            else:
                P[i] = 0  # 如果超出了 R，老老实实从 0 开始扩展

            # 以 i 为中心，尝试向左右两边扩展
            # T[i + 1 + P[i]] 是右侧下一个字符，T[i - 1 - P[i]] 是左侧下一个字符
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1  # 以i为中心的最长回文半径+1

            # 第三步：如果新计算出的回文边界超过了目前的 R，则更新 C 和 R
            if i + P[i] > R:  # 中心坐标+半径>原来的最右回文边界
                C = i
                R = i + P[i]

            # 记录全局最长回文串的信息
            if P[i] > max_len:
                max_len = P[i]
                center_index = i

        # 第四步：根据中心点和最大长度，从原字符串中截取结果
        start = (center_index - max_len) // 2
        return s[start: start + max_len]


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
