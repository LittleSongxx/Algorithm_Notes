n = int(input())
height = list(map(int, input().split()))

left = 0
right = n - 1
ans = 0

while left < right:
    area = (right - left) * min(height[left], height[right])
    ans = max(ans, area)

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(ans)
