def lis(nums):
    tails = []  # tails[i]表示长度为 i+1 的上升子序列，结尾最小可以是多少。
    n = len(nums)
    res = [0] * n  # res[i] 表示：以 nums[i] 结尾的最长严格上升子序列长度
    for i in range(n):
        x = nums[i]
        left = 0
        right = len(tails) - 1
        # 在tails数组中找到第一个 >= x 的位置
        while left <= right:
            mid = (left + right) // 2
            if tails[mid] >= x:  # 要找的是第一个 >= x 的位置，现在mid及右边的都是比x大的，所以第一个不可能在右边
                right = mid - 1  # 去左边找
            else:
                left = mid + 1
        if left == len(tails):  # x比tails里的都大，接到tails后面
            tails.append(x)
        else:
            tails[left] = x  # 用x覆盖找到的位置的元素，因为x是刚好比这个位置小但又能保持整个tail数组递增的，换成更小的x能够使得他后面能容纳更多满足递增的数
        res[i] = left + 1
    return res

n = int(input())
a = list(map(int, input().split()))
up = lis(a)
down = lis(a[::-1])[::-1]
ans = 0
for i in range(n):
    if up[i] > 1 and down[i] > 1:
        ans = max(ans, up[i] + down[i] - 1)
print(ans)