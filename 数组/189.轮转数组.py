from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        k %= n  # 轮转 k 次等于轮转 k % n 次
        reverse(0, n - 1)  # 全部翻转
        reverse(0, k - 1)  # 翻转前k个
        reverse(k, n - 1)  # 翻转后n-k个


if __name__ == '__main__':
    pass
