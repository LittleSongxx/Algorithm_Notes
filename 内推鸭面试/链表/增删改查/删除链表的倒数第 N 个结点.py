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


def remove(head, n):
    dummy = ListNode(-1, head)
    fast = dummy
    slow = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next


def print_list(head):
    ans = []
    while head:
        ans.append(str(head.val))
        head = head.next
    print(" ".join(ans))


if __name__ == "__main__":
    sz = int(input())
    nodes = list(map(int, input().split()))
    n = int(input())
    head = build_list(nodes)
    head = remove(head, n)
    print_list(head)
