def check(x, wood, k):
    cnt = 0
    for length in wood:
        cnt += length // x
    return cnt >= k


n, k = map(int, input().split())
wood = [int(input()) for _ in range(n)]

# 如果连 1cm 都切不出 k 段，直接输出 0
if sum(wood) < k:
    print(0)
else:
    l, r = 1, max(wood)

    while l < r:
        mid = (l + r + 1) // 2  # 取上中位数，防止死循环
        if check(mid, wood, k):
            l = mid
        else:
            r = mid - 1

    print(l)
