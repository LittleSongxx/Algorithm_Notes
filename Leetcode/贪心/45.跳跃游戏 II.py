class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        # 如果数组长度为1，已经在终点了，不需要跳跃
        if n == 1:
            return 0

        jumps = 0
        current_end = 0  # 当前这步跳跃能到达的右边界
        max_reach = 0  # 在当前边界内，能探索到的最远位置

        # 注意：这里遍历到 n - 1 即可，不需要遍历最后一个元素
        # 因为题目保证一定能到达，如果走到最后一个元素再触发边界，会多算一次跳跃
        for i in range(n - 1):
            # 持续更新能到达的最远位置
            max_reach = max(max_reach, i + nums[i])

            # 如果走到了当前跳跃的右边界
            if i == current_end:
                jumps += 1  # 必须跳下一次了
                current_end = max_reach  # 更新下一次跳跃的右边界

                # 提前结束
                if max_reach >= n - 1:
                    break

        return jumps


if __name__ == "__main__":
    pass
