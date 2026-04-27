n = int(input())
nums = list(map(int, input().split()))

num_set = set(nums)

ans = 0

for x in num_set:
    # 只有不是起点的值才计算，否则这个数一定是接在前面的数后面，最大值不会更大
    if x - 1 not in num_set:
        cur = x
        length = 1
        # 依次判断后面的数是否能继续接在后面
        while cur + 1 in num_set:
            cur += 1
            length += 1

        ans = max(ans, length)

print(ans)
