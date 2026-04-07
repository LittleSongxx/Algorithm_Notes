n = int(input())
w = list(map(int, input().split()))
res = 0  # 最大长度
l = 0
while l < n:
    r = l
    # 如果下一个元素大于当前元素，右边界向右移动
    while r + 1 < n and w[r + 1] > w[r]:
        r += 1
    # 更新最大长度
    res = max(res, r - l + 1)
    l = r + 1
print(res)
