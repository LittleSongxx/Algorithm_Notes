class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(nodes):
    dummy = ListNode()
    cur = dummy

    for x in nodes:
        cur.next = ListNode(x)
        cur = cur.next

    return dummy.next


def swap_per_k(head, k):
    dummy = ListNode(0, head)
    prev_group_tail = dummy  # 始终指向“上一组翻转后”的尾结点

    while True:
        # kth 表示“当前这一组的第 k 个结点”，也就是当前组的尾结点
        kth = prev_group_tail

        # 从上一组的尾巴 prev_group_tail 开始，往后走 k 步，找到这一组的最后一个结点
        for _ in range(k):
            kth = kth.next
            # 不够k个，这一组不翻转，直接结束
            if not kth:
                return dummy.next

        group_head = prev_group_tail.next  # 当前组的头
        next_group_head = kth.next  # 下一组的头

        # 翻转区间 [group_head, kth]
        prev = next_group_head  # 这一组的头翻转完要指向下一组的头，所有prev初始指向下一组的头
        cur = group_head
        while cur != next_group_head:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # 翻转后：
        # kth 成为这一组的新头
        # group_head 成为这一组的新尾
        prev_group_tail.next = kth
        prev_group_tail = group_head


def print_list(head):
    ans = []
    while head:
        ans.append(str(head.val))
        head = head.next
    print(" ".join(ans))


if __name__ == "__main__":
    nodes = list(map(int, input().split()))
    k = int(input())

    head = build_list(nodes)
    head = swap_per_k(head, k)
    print_list(head)
