import heapq


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


def merge_k_lists(lists):
    # 用小根堆构造优先级队列
    heap = []
    uid = 0  # 当 val 相同时，用 uid 避免 Python 继续比较 ListNode 对象

    # 先把每个链表的头结点放入最小堆
    for node in lists:
        if node:
            # node.val：主要比较依据，值越小优先级越高
            # uid：辅助比较，防止值相同时出错
            # node：真正的链表节点对象
            heapq.heappush(heap, (node.val, uid, node))
            uid += 1
    dummy = ListNode()
    cur = dummy

    # 每次取出当前最小节点，接到结果链表后面
    while heap:
        _, _, node = heapq.heappop(heap)

        cur.next = node
        cur = cur.next

        # 把该节点的下一个节点放入堆中，会自动排序得到最小的队头
        if node.next:
            heapq.heappush(heap, (node.next.val, uid, node.next))
            uid += 1  # 在节点值相同时，后入队的优先级更低

    return dummy.next
