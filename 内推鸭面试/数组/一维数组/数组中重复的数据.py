n = int(input())
nums = list(map(int, input().split()))

ans = []

for x in nums:
    # 以数组当前值为哈希表的下标
    idx = abs(x) - 1
    # 已经是反的则说明是第二次出现了，加入结果集
    if nums[idx] < 0:
        ans.append(abs(x))
    # 第一次遇见该数，则将其对应位置取反
    else:
        nums[idx] = -nums[idx]

ans.sort()
print(' '.join(map(str, ans)))
