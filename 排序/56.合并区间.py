from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda p: p[0])  # 按左边界排序
        ans = []
        for p in intervals:  # p遍历二维嵌套list，p是intervals里的每一个一维list
            # ans[-1]: 以负的索引表示结果列表中的最后一个区间，ans[-1][1]: 结果列表中最后一个区间的结束位置
            # 例如ans=[[1,2],[3,6]]时，ans[-1][1]表示取[3,6]中的第1个位置，即6
            if ans and p[0] <= ans[-1][1]:  # 合并的前提是遇到的新区间左端点不超过ans里的最大右端点，即相交
                ans[-1][1] = max(ans[-1][1], p[1])  # 更新右端点最大值，因为是合并，所以直接修改ans
            else:  # 不相交，无法合并
                ans.append(p)  # 将新的区间追加进ans里，作为一个子list
        return ans


if __name__ == '__main__':
    pass
