n = int(input())
nums = list(map(int, input().split()))

left, right = 0, n - 1

while left < right:
    mid = (left + right) // 2

    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid  # 最小值可能就是mid，不能写right = mid - 1

print(nums[left])
