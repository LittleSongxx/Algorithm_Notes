from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0  # 全局变量，记录扫描过程中遇到的最大直径

        # 辅助函数：求二叉树的最大深度
        def depth(node):
            nonlocal max_diameter

            # Base case：空节点的深度为 0
            if not node:
                return 0

            # 1. 递归求左右子树的最大深度
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # 2. 核心操作：计算以当前节点为拐点的路径长度，并更新全局最大值
            # 这里的长度恰好就是 left_depth + right_depth (代表边数)
            max_diameter = max(max_diameter, left_depth + right_depth)

            # 3. 向上返回当前节点的最大深度
            return max(left_depth, right_depth) + 1

        # 触发递归计算
        depth(root)
        return max_diameter

if __name__ == '__main__':
    pass
