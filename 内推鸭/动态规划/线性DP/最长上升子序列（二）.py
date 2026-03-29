n = int(input())
nums = list(map(int, input().split()))

# tails[i] 表示：
# 长度为 i+1 的上升子序列中，结尾最小可以是多少
tails = []

for x in nums:
    # 如果 tails 还是空的，或者当前数比 tails 最后一个还大
    # 说明它可以直接接在当前最长上升子序列后面
    if len(tails) == 0 or x > tails[-1]:
        tails.append(x)
    else:
        # 否则，当前数不能直接接到最后
        # 我们就用二分查找，找到 tails 中第一个 >= x 的位置
        # 然后用 x 替换它
        # 这样不会改变当前最长长度, 但可以让对应长度的子序列“结尾更小”，方便后面接更多数

        left = 0
        right = len(tails) - 1

        while left < right:
            mid = (left + right) // 2

            if tails[mid] >= x:
                # 说明答案在 mid 或者 mid 左边
                right = mid
            else:
                # 说明 mid 这个位置太小了，要去右边找
                left = mid + 1

        # left 最终就是第一个 >= x 的位置
        tails[left] = x

# tails 的长度就是最长上升子序列的长度
print(len(tails))
