n, target = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = n - 1

while left <= right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print(left)
