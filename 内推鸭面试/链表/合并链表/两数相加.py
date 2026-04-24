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


def addTwoNums(l1, l2):
    carry = 0

    head3 = ListNode()
    dummy = head3
    while l1 or l2 or carry:
        sum = carry
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        head3.next = ListNode(sum % 10)
        head3 = head3.next
        carry = sum // 10
    return dummy.next


def print_list(head):
    ans = []
    while head:
        ans.append(str(head.val))
        head = head.next
    print(" ".join(ans))


n = int(input())
for _ in range(n):
    cnt1 = int(input())
    node1 = list(map(int, input().split()))
    l1 = build_list(node1)

    cnt2 = int(input())
    node2 = list(map(int, input().split()))
    l2 = build_list(node2)

    res = addTwoNums(l1, l2)
    print_list(res)
