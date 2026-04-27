n, target = map(int, input().split())
nums = list(map(int, input().split()))


def find(nums, target):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


print(find(nums, target))
