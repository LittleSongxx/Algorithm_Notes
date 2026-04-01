def check(x, a, b, n):
    # 判断当前答案x是否满足条件
    return (a // x + b // x) >= n


n, a, b = map(int, input().split())

l, r = 1, (a + b) // n  # 枚举的是每个小孩最多得到的糖果数，每个小孩又都需要分到，所以右边界设置为均分到每个小孩得到的个数
while l < r:
    mid = (l + r + 1) // 2  # +1是为了防止l死循环不更新
    if check(mid, a, b, n):
        l = mid
    else:
        r = mid - 1
print(l)
