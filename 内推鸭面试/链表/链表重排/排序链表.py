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


# 合并两个有序链表
def merge(l1, l2):
    dummy = ListNode()
    cur = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    # 剩下的直接整段解在cur后面
    cur.next = l1 if l1 else l2
    return dummy.next


def sort_list(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = None

    left = sort_list(head)
    right = sort_list(slow)

    return merge(left, right)


def print_list(head):
    ans = []
    while head:
        ans.append(str(head.val))
        head = head.next
    print(" ".join(ans))


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    head = build_list(nums)
    head = sort_list(head)
    print_list(head)
