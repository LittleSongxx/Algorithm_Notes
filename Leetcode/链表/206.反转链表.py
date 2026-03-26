from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next  # 防止下一步cur.next指回pre时与后一个数断开
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


if __name__ == "__main__":
    pass
