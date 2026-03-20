from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root

        while curr:
            # 如果左子树不为空，才需要进行“搭桥”和“转移”操作
            if curr.left:
                pre = curr.left
                # 1. 找左子树的最右节点 (这就是前序遍历时左子树的最后一个节点)
                while pre.right:
                    pre = pre.right

                # 2. 搭桥：把原来的右子树接到 pre 的右边
                pre.right = curr.right

                # 3. 转移：把左子树整个移到右边
                curr.right = curr.left

                # 4. 置空：左子树一定要记得置空
                curr.left = None

            # 处理下一个节点 (注意：此时 curr.right 已经是原来的 curr.left 了)
            curr = curr.right


if __name__ == '__main__':
    pass
