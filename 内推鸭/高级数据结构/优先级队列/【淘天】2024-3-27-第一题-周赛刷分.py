import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 建小根堆
heapq.heapify(a)

# 当前所有账号的最大分数
mx = max(a)

for add in b:
    # 取出当前最小分数的账号
    x = heapq.heappop(a)

    # 比赛后分数增加
    new_score = x + add

    # 放回堆中
    heapq.heappush(a, new_score)

    # 更新最大值
    if new_score > mx:
        mx = new_score

    print(mx)
