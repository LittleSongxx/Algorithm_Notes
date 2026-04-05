def check(x, a, n, k, l):
    used = 0          # 已经用了多少次训练
    cover = -1        # 当前已经覆盖到的最右位置

    for i in range(n):
        # 如果这个位置已经达标，或者已经被前面的训练覆盖，就不用管
        if a[i] >= x or i <= cover:
            continue

        # 这个位置不达标且没被覆盖，必须新开一次训练
        used += 1
        cover = i + l - 1

        if used > k:
            return False

    return True


n, k, l = map(int, input().split())
a = list(map(int, input().split()))

left, right = 1, max(a)

while left < right:
    mid = (left + right + 1) // 2
    if check(mid, a, n, k, l):
        left = mid
    else:
        right = mid - 1

print(left)
