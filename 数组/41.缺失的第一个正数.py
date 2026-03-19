from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # 1. 遍历数组，让数字回到本应该在的位置
        for i in range(n):
            # 满足两个条件才交换：
            # 1. 数字必须在 [1, n] 的范围内
            # 2. 数字没在它该在的位置上 (nums[i] != nums[nums[i] - 1])，例如4应该在下标3的位置
            # 使用 while 是因为换过来的新数字可能还需要继续被交换到它该去的地方
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # 把 nums[i] 放到正确的索引 (nums[i] - 1) 上去
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # 2. 再次遍历找茬
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1  # 遇到第一个位置不对的，说明 i+1 缺失了

        # 3. 如果全都正确，说明数组是 [1, 2, 3, ..., n]
        # 缺失的是 n + 1
        return n + 1


if __name__ == "__main__":
    pass
