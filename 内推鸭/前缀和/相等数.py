n = int(input())
a = list(map(int, input().split()))

# 1. 保存 (数值, 原下标)
nums = []
for i in range(n):
    nums.append((a[i], i))

# 2. 按数值排序
# 排序完是（数值，原下标）
# 例如[(2, 0), (1, 1), (4, 2)]排序完后变成[(1, 1), (2, 0), (4, 2)]
nums.sort()

# 3. 提取排序后的数值
sorted_values = [0] * n
for i in range(n):
    sorted_values[i] = nums[i][0]

# 4. 计算前缀和
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + sorted_values[i - 1]

# 5. 计算每个位置的答案
answer = [0] * n

for k in range(n):
    value = nums[k][0]
    original_index = nums[k][1]

    left_cost = value * k - prefix[k]
    right_cost = (prefix[n] - prefix[k + 1]) - value * (n - k - 1)

    answer[original_index] = left_cost + right_cost

# 6. 按原顺序输出
for x in answer:
    print(x)
