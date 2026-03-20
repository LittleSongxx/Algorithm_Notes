from turtledemo.penrose import start
from typing import List, Optional

from PIL.TiffImagePlugin import idx
from cytoolz.itertoolz import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque([root])
        ans = []
        while queue:
            level_len = len(queue)

            for i in range(level_len):
                curr = queue.popleft()
                if i == level_len - 1:
                    ans.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return ans

    def rightSideView_v2(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node, depth):
            if not node:
                return
            if depth == len(ans):
                ans.append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return ans


if __name__ == '__main__':
    pass
