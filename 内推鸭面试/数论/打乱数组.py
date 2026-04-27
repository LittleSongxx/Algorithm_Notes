import random


class Solution:

    def __init__(self, nums):
        # 保存原始数组
        self.original = nums[:]
        # 保存当前数组
        self.nums = nums[:]

    def reset(self):
        # 恢复成原始数组
        self.nums = self.original[:]
        return self.nums

    def shuffle(self):
        # 复制一份数组来打乱
        arr = self.original[:]
        n = len(arr)

        # Fisher-Yates 洗牌算法
        for i in range(n):
            j = random.randint(i, n - 1)
            arr[i], arr[j] = arr[j], arr[i]

        return arr
