from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = dummy.next
        pre = dummy
        while curr.next and curr.next.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = curr
            pre.next = temp
            pre = curr
            curr = curr.next
        return dummy



if __name__ == "__main__":
    pass
