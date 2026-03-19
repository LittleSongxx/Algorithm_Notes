class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder_recursive(root):
        """前序遍历：根 -> 左 -> 右"""
        res = []

        def dfs(node):
            if not node: return
            res.append(node.val)  # 1. 记录根节点
            dfs(node.left)  # 2. 遍历左子树
            dfs(node.right)  # 3. 遍历右子树

        dfs(root)
        return res

    def inorder_recursive(root):
        """中序遍历：左 -> 根 -> 右"""
        res = []

        def dfs(node):
            if not node: return
            dfs(node.left)  # 1. 遍历左子树
            res.append(node.val)  # 2. 记录根节点
            dfs(node.right)  # 3. 遍历右子树

        dfs(root)
        return res

    def postorder_recursive(root):
        """后序遍历：左 -> 右 -> 根"""
        res = []

        def dfs(node):
            if not node: return
            dfs(node.left)  # 1. 遍历左子树
            dfs(node.right)  # 2. 遍历右子树
            res.append(node.val)  # 3. 记录根节点

        dfs(root)
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    s = Solution

    print("=== 递归遍历 ===")
    print("前序:", s.preorder_recursive(root))  # 预期: [1, 2, 4, 5, 3, 6]
    print("中序:", s.inorder_recursive(root))  # 预期: [4, 2, 5, 1, 3, 6]
    print("后序:", s.postorder_recursive(root))  # 预期: [4, 5, 2, 6, 3, 1]
