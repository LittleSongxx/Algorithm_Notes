from typing import List


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # 1. 记录每个字符最后一次出现的下标
        # enumerate 会生成 (下标, 字符) 的对
        # 每当遇到一个新的(下标, 字符) 的对时覆盖原来的，所以最终last_occurrence里存的就是每个字符的最后一次出现的下标
        last_occurrence = {char: i for i, char in enumerate(s)}

        result = []
        start = 0  # 当前片段的起始位置
        end = 0  # 当前片段必须到达的最远边界

        # 2. 遍历字符串，寻找切割点
        for i, char in enumerate(s):
            # 贪心策略：当前片段的边界，必须能包容当前字符的最后一次出现位置
            end = max(end, last_occurrence[char])

            # 如果当前下标走到了必须到达的最远边界，说明可以切一刀了
            if i == end:
                # 计算当前片段的长度并加入结果
                result.append(end - start + 1)
                # 更新下一个片段的起始位置
                start = i + 1

        return result


if __name__ == "__main__":
    pass
