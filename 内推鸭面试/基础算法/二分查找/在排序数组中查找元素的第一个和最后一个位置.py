n = int(input())
nums = list(map(int, input().split())) if n > 0 else []
target = int(input())

def find_first(nums, target):
    left, right = 0, len(nums) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            ans = mid
            right = mid - 1   # 继续往左找，确保是最左边的
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans

def find_last(nums, target):
    left, right = 0, len(nums) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            ans = mid
            left = mid + 1    # 继续往右找，确保是最右边的
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans

first = find_first(nums, target)
last = find_last(nums, target)

print(first, last)
