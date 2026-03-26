from platform import node
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def check(left, right):
            # 都为空也认为对称
            if not left and not right:
                return True
            # 两边只有一个空，或者值不一样，认为不对称
            if not left or not right or left.val != right.val:
                return False
            return check(left.left, right.right) and check(left.right, right.left)

        return check(root.left, root.right)


if __name__ == '__main__':
    s = Solution()
    print(s.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))))
    print(s.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), None))))
