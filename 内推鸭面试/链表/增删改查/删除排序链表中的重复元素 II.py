class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(nodes):
    dummy = ListNode()
    cur = dummy

    for x in nodes:
        cur.next = ListNode(x, None)
        cur = cur.next

    return dummy.next


def print_list(head):
    ans = []

    while head:
        ans.append(head.val)
        head = head.next

    print(''.join(str(ans)))


def remove_dup(head):
    dummy = ListNode()
    dummy.next = head

    cur = dummy

    while cur.next and cur.next.next:
        # 后面两个数相同
        if cur.next.val == cur.next.next.val:
            dup_val = cur.next.val
            # 一直往后遍历，跳过所有值相同的节点
            while cur.next and cur.next.val == dup_val:
                cur.next = cur.next.next
        else:
            cur = cur.next

    return dummy.next


n = int(input())
nodes = list(map(int, input().split()))

head = build_list(nodes)
head = remove_dup(head)
print_list(head)
