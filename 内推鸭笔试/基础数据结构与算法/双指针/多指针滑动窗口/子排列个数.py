n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 只需要记录 b 数组中元素的索引位置
# 为了方便计算，索引直接从 0 开始记录
pos2 = [0] * (n + 1)
for i in range(n):
    pos2[b[i]] = i

res = n * (n + 1)  # 总方案数

# 只需要一层 for 循环遍历 a 数组
current_len = 1
for i in range(1, n):
    # 核心判断：a 当前元素在 b 中的位置，是否刚好紧挨着 a 前一个元素在 b 中的位置
    if pos2[a[i]] == pos2[a[i - 1]] + 1:
        current_len += 1
    else:
        # 如果不是紧挨着的，说明连续中断了，结算刚才那一段的重叠数
        res -= current_len * (current_len + 1) // 2
        current_len = 1  # 重新开始计数

# 【改动3】循环结束后，别忘了最后一段还要结算一次
res -= current_len * (current_len + 1) // 2

print(res)
