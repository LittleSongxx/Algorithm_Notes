R = list(map(int, input().split()))
limit = int(input())

def check(x, R, limit):
    total = 0
    for r in R:
        total += min(r, x)
    return total <= limit


if sum(R) <= limit:
    print(-1)  # 不必限流
else:
    l, r = 0, max(R)
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid, R, limit):
            l = mid
        else:
            r = mid - 1
    print(l)
