from tokenize import group
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy  # pre 永远指向当前即将翻转的这一组的“前驱节点”

        while True:
            # 1. 探路：检查剩下的节点够不够 K 个
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    # 不够 K 个了，直接返回最终结果
                    return dummy.next

            # 2. 标记关键节点
            group_head = pre.next  # 当前组里的第一个节点
            nxt_group = tail.next  # 下一组里的第一个节点

            # 3. 核心翻转逻辑（高能技巧 ⚠️）
            # 平时我们翻转，prev 初始为 None。
            # 这里我们直接把 prev 初始设定为 nxt_group！
            # 这样在翻转的过程中，这一组原本的头（现在的尾）在第一次调转方向时，就直接连上了后面的链表！
            prev_node = nxt_group
            curr = group_head

            # 实打实地翻转 K 次
            for _ in range(k):
                nxt = curr.next
                curr.next = prev_node  # 调转箭头
                prev_node = curr  # 和常规的翻转链表逻辑一样，只不过prev_node初始化为nxt_group，而不是常规的None
                curr = nxt  # curr 步进

            # 4. 缝合前驱节点
            # 循环结束后，prev_node 从本组的最后一个变成了第一个，也就是pre的下一个，第一次翻转时就是接到了dummy的后面
            pre.next = prev_node

            # 5. pre 移动到当前这组的新尾巴上，准备开启下一组的循环
            # 此时的group_head还没有更新，还是原来的本组的第一个，只不过此时经过翻转第一个变成了本组的最后一个，而本组最后一个又可视为下一组全组的前驱节点
            pre = group_head


if __name__ == "__main__":
    pass
