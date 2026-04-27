def find_median_sorted_arrays(nums1, nums2):
    # 保证 nums1 是更短的数组，方便二分
    # 在短数组上二分，长数组配合它
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    half = (m + n + 1) // 2  # 合并后的左半边总共要放多少个数

    left, right = 0, m

    while left <= right:
        i = (left + right) // 2  # nums1 左边左边放i个，由于在num1上二分，所以i直接取一半
        j = half - i  # nums2 左边取 j 个，num2配合num1，所以j只需要算剩下还要多少

        # 处理边界
        # left1：nums1 左半边最后一个数
        # right1：nums1 右半边第一个数
        # left2：nums2 左半边最后一个数
        # right2：nums2 右半边第一个数
        left1 = float('-inf') if i == 0 else nums1[i - 1]
        right1 = float('inf') if i == m else nums1[i]
        left2 = float('-inf') if j == 0 else nums2[j - 1]
        right2 = float('inf') if j == n else nums2[j]

        # 找到正确划分
        if left1 <= right2 and left2 <= right1:  # 这是为了满足左半边所有数 <= 右半边所有数
            if (m + n) % 2 == 1:  # 奇数的情况
                return float(max(left1, left2))  # 中位数就是左边最大值
            else:  # 偶数的情况
                # 中位数就是中间两个数的平均值
                # = (左边最大值 + 右边最小值) / 2
                return (max(left1, left2) + min(right1, right2)) / 2.0

        # nums1 左边拿太多了，切口 i 应该往左移：
        elif left1 > right2:
            right = i - 1

        # nums1 左边拿太少了，切口 i 应该往右移：
        else:
            left = i + 1


m = int(input())
nums1 = list(map(int, input().split())) if m > 0 else []
n = int(input())
nums2 = list(map(int, input().split())) if n > 0 else []

ans = find_median_sorted_arrays(nums1, nums2)
print(f"{ans:.5f}")
