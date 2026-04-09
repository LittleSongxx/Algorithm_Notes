n = int(input())
nums = list(map(int, input().split()))

left, right = 0, n - 1

while left < right:
    mid = (left + right) // 2
    if nums[mid] < nums[mid + 1]:
        left = mid + 1
    else:
        right = mid

print(left)
