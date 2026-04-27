class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def build_list(nums):
    dummy = ListNode()
    cur = dummy
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


def reverse_list(head):
    prev = None
    cur = head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev


def is_palidrome(head):
    if not head or not head.next:
        return True

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    right = reverse_list(slow)
    p1 = head
    p2 = right

    while p2:
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next

    return True


n = int(input())
nums = list(map(int, input().split()))
head = build_list(nums)

print("true" if is_palidrome(head) else "false")
