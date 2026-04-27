from math import inf

n, target = map(int, input().split())
nums = list(map(int, input().split()))

ans = inf

left = 0
total = 0

# 右指针扩展窗口
for right in range(n):
    total += nums[right]

    # 只要当前窗口满足条件，就尝试缩小左边界
    while total >= target:
        ans = min(ans, right - left + 1)
        # 收缩左窗口
        total -= nums[left]
        left += 1

if ans == inf:
    print(0)
else:
    print(ans)
