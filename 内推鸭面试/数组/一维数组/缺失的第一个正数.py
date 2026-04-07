n = int(input())
nums = list(map(int, input().split()))

for i in range(n):
    # 只要当前数字在 1~n 范围内，并且它没有在正确位置上，就继续交换
    while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
        correct_index = nums[i] - 1
        # 交换到正确的位置
        nums[i], nums[correct_index] = nums[correct_index], nums[i]

for i in range(n):
    if nums[i] != i + 1:  # 第一个没在正确位置的
        print(i + 1)
        break
else:
    print(n + 1)
