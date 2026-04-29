class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


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


def change_list(head):
    odd = head  # 奇
    even = head.next  # 偶
    even_head = even  # 保存偶数链表头节点 2

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head


n = int(input())
if n == 0:
    print()
else:
    nodes = list(map(int, input().split()))
    head = build_list(nodes)
    head = change_list(head)
    print_list(head)
