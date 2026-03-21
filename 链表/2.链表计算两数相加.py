from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0  # 进位初始为 0

        # 只要 l1 没走完，或者 l2 没走完，或者还有进位没处理，就继续加！
        while l1 or l2 or carry:
            # 1. 安全取值：如果链表节点为空，说明这一位是 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # 2. 计算当前位的总和与新的进位
            total = val1 + val2 + carry
            carry = total // 10  # Python 的整除，用来求进位 (比如 15 // 10 = 1)
            remainder = total % 10  # 取余数，用来做当前节点的值 (比如 15 % 10 = 5)

            # 3. 创建新节点，并挂到 curr 后面
            curr.next = ListNode(remainder)

            # 4. 所有游标往前走一步
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


if __name__ == "__main__":
    pass
