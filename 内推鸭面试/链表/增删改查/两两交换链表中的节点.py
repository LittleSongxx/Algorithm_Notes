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


def swap_pairs(head):
    dummy = ListNode(-1, head)
    prev = dummy

    while prev.next and prev.next.next:
        a = prev.next
        b = prev.next.next

        a.next = b.next
        b.next = a
        prev.next = b

        prev = a

    return dummy.next


def print_list(head):
    ans = []
    while head:
        ans.append(str(head.val))
        head = head.next
    print(" ".join(ans))


if __name__ == "__main__":
    sz = int(input())
    nodes = []
    while len(nodes) < sz:
        nodes.extend(map(int, input().split()))
    head = build_list(nodes)
    head = swap_pairs(head)
    print_list(head)
