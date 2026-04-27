nums = list(map(int, input().split()))

candidate1 = None
candidate2 = None
count1 = 0
count2 = 0

for x in nums:
    # 候选人票数+1
    if x == candidate1:
        count1 += 1
    elif x == candidate2:
        count2 += 1
    # 重置候选人
    elif count1 == 0:
        candidate1 = x
        count1 = 1
    elif count2 == 0:
        candidate2 = x
        count2 = 1
    # 不是支持者，减票
    else:
        count1 -= 1
        count2 -= 1

# 验证是否超过1/3
ans = []
n = len(nums)

if nums.count(candidate1) > n // 3:
    ans.append(candidate1)

if candidate2 != candidate1 and nums.count(candidate2) > n // 3:
    ans.append(candidate2)

print(ans)
