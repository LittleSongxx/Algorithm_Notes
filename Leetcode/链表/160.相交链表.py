from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node1 = headA
        node2 = headB
        len_A = len_B = 0
        while node1:
            node1 = node1.next
            len_A += 1
        while node2:
            node2 = node2.next
            len_B += 1

        if len_B > len_A:
            temp = headA
            headA = headB
            headB = temp
        distance = len_A - len_B
        while distance > 0:
            headA = headA.next
            distance -= 1
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None


if __name__ == "__main__":
    pass
