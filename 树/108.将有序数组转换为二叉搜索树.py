from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        # 辅助函数，用来处理指定区间 [left, right] 内的数组元素
        def build_bst(left: int, right: int) -> Optional[TreeNode]:
            # Base case: 如果左边界越过了右边界，说明区间内没有元素了，返回空节点
            if left > right:
                return None

            # 1. 找中点作为根节点 (如果区间长度是偶数，这里倾向于选择左中间节点)
            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            # 2. 递归构建左子树 (范围是中点左边的所有元素)
            root.left = build_bst(left, mid - 1)

            # 3. 递归构建右子树 (范围是中点右边的所有元素)
            root.right = build_bst(mid + 1, right)

            return root

        # 初始调用，传入整个数组的完整区间
        return build_bst(0, len(nums) - 1)


if __name__ == '__main__':
    pass
