n = int(input())
height = list(map(int, input().split()))

if n == 0:
    print(0)
else:
    left_max = [0] * n
    right_max = [0] * n

    # 求前缀最大值
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    # 求后缀最大值
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    ans = 0
    for i in range(n):
        ans += min(left_max[i], right_max[i]) - height[i]

    print(ans)
