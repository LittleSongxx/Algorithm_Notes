def find_duplicate(nums):
    slow = 0
    fast = 0

    # 找相遇点
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    # 找环入口
    enter = 0

    while enter != slow:
        enter = nums[enter]
        slow = nums[slow]

    return enter


n = int(input())
nums = list(map(int, input().split()))

print(find_duplicate(nums))
