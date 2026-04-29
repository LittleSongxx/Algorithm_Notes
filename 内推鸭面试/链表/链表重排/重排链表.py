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


def print_list(head):
    ans = []
    while head:
        ans.append(str(head.val))
        head = head.next
    print(" ".join(ans))


def reverse_list(head):
    prev = None
    cur = head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def change_list(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    r = slow.next  # 从中间拆分两个链表
    slow.next = None

    r = reverse_list(r)

    l = head

    while r:
        l_next = l.next
        r_next = r.next

        l.next = r
        r.next = l_next

        l = l_next
        r = r_next

    return head


n = int(input())
nodes = list(map(int, input().split()))
head = build_list(nodes)
head = change_list(head)
print_list(head)
