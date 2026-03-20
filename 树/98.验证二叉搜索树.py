from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 辅助函数，携带当前节点允许的下界和上界
        def validate(node, left, right):
            # 空节点也是合法的 BST
            if not node:
                return True

            # 违反了 BST 的严格大小关系（注意是严格大于/小于，所以带等号就 return False）
            if node.val <= left or node.val >= right:
                return False

            # 递归检查左子树（更新上界）和右子树（更新下界）
            return validate(node.left, left, node.val) and validate(node.right, node.val, right)

        # 初始时，根节点的值可以是任意大小，使用 Python 的正负无穷大
        return validate(root, float('-inf'), float('inf'))

    def isValidBST_v2(self, root: Optional[TreeNode]) -> bool:
        stack = []
        curr = root
        # 记录中序遍历序列中的前一个值，初始设为负无穷
        pre_val = float('-inf')

        while curr or stack:
            # 1. 一路向左，把左边界全压入栈
            while curr:
                stack.append(curr)
                curr = curr.left

            # 2. 走到尽头，弹出节点进行处理
            curr = stack.pop()

            # 核心判断：如果当前节点的值没有严格大于上一个节点的值，说明不是递增的，直接 False
            if curr.val <= pre_val:
                return False

            # 更新 pre_val 为当前节点的值
            pre_val = curr.val

            # 3. 转向右子树
            curr = curr.right

        return True


if __name__ == '__main__':
    print(Solution().isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))))
