class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 前序遍历
    def preorder_iterative(root):
        if not root: return []
        stack = [root]
        res = []

        while stack:
            node = stack.pop()  # 弹出栈顶节点
            res.append(node.val)  # 记录值

            # 注意压栈顺序：先右后左，这样出栈才是先左后右
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res

    # 中序遍历
    def inorder_iterative(root):
        stack = []
        res = []
        curr = root

        while curr or stack:
            # 一直向左走，把左边界全部压入栈
            while curr:
                stack.append(curr)
                curr = curr.left

            # 走到尽头，弹出节点，记录值
            curr = stack.pop()
            res.append(curr.val)

            # 转向右子树
            curr = curr.right

        return res

    def postorder_iterative(root):
        if not root: return []
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)

            # 压栈顺序：先左后右（这样出栈才是先右后左）
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # 此时 res 里是 根->右->左，利用 Python 切片直接翻转列表
        return res[::-1]


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    s = Solution

    print("=== 非递归迭代遍历 ===")
    print("前序:", s.preorder_iterative(root))   # 预期: [1, 2, 4, 5, 3, 6]
    print("中序:", s.inorder_iterative(root))    # 预期: [4, 2, 5, 1, 3, 6]
    print("后序:", s.postorder_iterative(root))  # 预期: [4, 5, 2, 6, 3, 1]
