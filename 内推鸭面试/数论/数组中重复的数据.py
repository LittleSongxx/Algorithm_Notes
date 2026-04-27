n = int(input())
nums = list(map(int, input().split()))

ans = []
for x in nums:
    idx = abs(x) - 1  # 由于当前数x可能已经被前面取负了，所以要先取绝对值
    if nums[idx] < 0:  # idx位置的数已经是负的了，说明x不是第一次出现
        ans.append(abs(x))  # 加入答案
    else:
        nums[idx] = -nums[idx]

print(*ans)
