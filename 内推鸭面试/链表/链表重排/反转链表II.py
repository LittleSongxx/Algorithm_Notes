class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(nums):
    dummy = ListNode()
    cur = dummy
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


def print_list(head):
    ans = []
    while head:
        ans.append(str(head.val))
        head = head.next
    print(" ".join(ans))


def reverse_between(head, left, right):
    if not head or left == right:
        return head

    dummy = ListNode()
    dummy.next = head

    # pre 指向反转区间的前一个节点
    pre = dummy
    for _ in range(left - 1):
        pre = pre.next

    # cur 指向反转区间的第一个节点
    cur = pre.next

    # 头插法反转 left 到 right 之间的节点
    for _ in range(right - left):
        nxt = cur.next

        cur.next = nxt.next
        nxt.next = pre.next
        pre.next = nxt

    return dummy.next


n, left, right = list(map(int, input().split()))
nums = list(map(int, input().split()))

head = build_list(nums)
head = reverse_between(head, left, right)

print_list(head)
