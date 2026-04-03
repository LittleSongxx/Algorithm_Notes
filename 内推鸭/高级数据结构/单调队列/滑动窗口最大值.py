from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

# 单调队列，存的是下标
q = deque()
result = []

for i in range(n):
    # 第一步：踢掉队列中比当前入队元素小的
    while q:
        if a[q[-1]] <= a[i]:  # 如果队尾元素 <= 当前元素，就踢掉
            q.pop()
        else:
            break

    # 第二步：把当前下标加到队尾
    q.append(i)

    # 第三步：踢头部
    # 如果队头的下标已经不在当前窗口 [i-k+1, i] 内，踢掉
    if q[0] < i - k + 1:
        q.popleft()

    # 第四步：记录答案
    # 当 i >= k-1 时，窗口已满，可以记录答案
    # 队头就是当前窗口的最大值的下标
    if i >= k - 1:
        result.append(str(a[q[0]]))

print(" ".join(result))
