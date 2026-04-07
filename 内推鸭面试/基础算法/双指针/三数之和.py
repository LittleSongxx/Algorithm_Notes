n = int(input())
nums = list(map(int, input().split()))

nums.sort()
ans = []

for i in range(n - 2):
    # 第一个数去重
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    # 剪枝1：排序后当前最小的数已经大于 0，后面的和不可能等于0
    if nums[i] > 0:
        break

    # 剪枝2：当前最小的三个数和都大于 0，后面更不可能
    if nums[i] + nums[i + 1] + nums[i + 2] > 0:
        break

    # 剪枝3：当前最大三个数和都小于 0，当前 i 不可能有解
    if nums[i] + nums[n - 2] + nums[n - 1] < 0:
        continue

    # 固定 nums[i] 后，另外两个数需要凑出的目标和
    target = -nums[i]

    left = i + 1
    right = n - 1

    while left < right:
        # 当前左右两个数的实际和
        two_sum = nums[left] + nums[right]

        if two_sum == target:
            ans.append([nums[i], nums[left], nums[right]])

            left += 1
            right -= 1

            # 去重
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1

        elif two_sum < target:
            left += 1
        else:
            right -= 1

for triple in ans:
    print(*triple)
