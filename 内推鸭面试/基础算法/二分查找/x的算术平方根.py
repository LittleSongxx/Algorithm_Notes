x = int(input())

left, right = 0, x
ans = 0

while left <= right:
    mid = (left + right) // 2

    # 用 mid <= x // mid 代替 mid * mid <= x，避免大数乘法问题
    if mid <= x // mid:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
