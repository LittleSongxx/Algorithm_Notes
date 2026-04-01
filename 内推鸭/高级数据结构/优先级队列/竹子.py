import heapq

n = int(input())
lengths = list(map(int, input().split()))

# Python 的 heapq 默认是小根堆
# 所以把所有数取相反数，就能模拟大根堆
max_heap = [-x for x in lengths]
heapq.heapify(max_heap)

# 当前最小值
current_min = min(lengths)

# 操作次数
operations = 0

# 当最大值 != 最小值时，说明还没有全部相等
while -max_heap[0] != current_min:
    # 取出当前最大值
    largest = -heapq.heappop(max_heap)

    # 砍掉一半后，剩下 floor(largest / 2)
    largest //= 2

    # 更新当前最小值
    current_min = min(current_min, largest)

    # 放回堆中
    heapq.heappush(max_heap, -largest)

    # 记录操作次数
    operations += 1

print(operations)
