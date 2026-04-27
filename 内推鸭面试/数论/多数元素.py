nums = list(map(int, input().split()))

candidate = None
count = 0

for x in nums:
    # 票数为 0 时，重新选择候选多数元素
    if count == 0:
        candidate = x

    # 相同则加票，不同则抵消
    if x == candidate:
        count += 1
    else:
        count -= 1

print(candidate)