n = int(input())
nums = list(map(int, input().split()))
target = int(input())

left, right = 0, n - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        print(mid)
        break
    # 落在了左半边有序区间
    if nums[left] <= nums[mid]:
        if nums[left] <= target <= nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    # 落在了右半边有序区间
    else:
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1
else:
    print(-1)