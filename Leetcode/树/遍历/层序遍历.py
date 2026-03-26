from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def level_order(root):
        if not root: return []

        queue = deque([root])
        res = []

        while queue:
            # 每次循环处理一整层的节点
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()  # 从左侧出队
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)  # 从右侧入队
                if node.right:
                    queue.append(node.right)

            res.append(current_level)  # 把这一层的列表装入最终结果

        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    s = Solution

    print("=== 层序遍历 ===")
    print("层序:", s.level_order(root))
