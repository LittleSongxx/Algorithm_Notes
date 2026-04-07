def check(x, a, n, m, k):
    # diff[i] 表示从位置 i 开始，累计加成发生的变化
    diff = [0] * (n + 1)

    add = 0  # 当前位置已经累计获得的攻击加成
    used = 0  # 已经使用的攻击次数

    for i in range(n):
        # 还原当前位置的累计加成
        add += diff[i]

        # 当前位置当前的实际流血状态
        cur = a[i] + add

        # 如果当前位置还没达到 x，就必须从这里补攻击
        if cur < x:
            need = x - cur

            # 从 i 开始的长度为 k 的区间必须合法
            if i + k > n:
                return False

            used += need
            if used > m:
                return False

            # 标准差分：区间 [i, i+k-1] 全部加 need
            diff[i] += need
            diff[i + k] -= need

            # 因为这一轮已经做过 add += diff[i]，
            # 所以新加的 need 要立刻补到 add 中
            add += need

    return True


n, m, k = map(int, input().split())
a = list(map(int, input().split()))

left = min(a)
right = max(a) + m

while left < right:
    mid = (left + right + 1) // 2
    if check(mid, a, n, m, k):
        left = mid
    else:
        right = mid - 1

print(left)
