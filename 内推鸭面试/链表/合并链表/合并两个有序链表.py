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


def merge(l1, l2):
    cur = ListNode(-1)
    dummy = cur
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = ListNode(l1.val)
            l1 = l1.next
        else:
            cur.next = ListNode(l2.val)
            l2 = l2.next
        cur = cur.next
    cur.next = l1 if l1 else l2
    return dummy.next

n = int(input())
for _ in range(n):
    cnt1 = int(input())
    node1 = list(map(int, input().split()))
    l1 = build_list(node1)

    cnt2 = int(input())
    node2 = list(map(int, input().split()))
    l2 = build_list(node2)

    res = merge(l1, l2)
    print_list(res)