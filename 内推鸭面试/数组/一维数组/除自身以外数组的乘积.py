n = int(input())
nums = list(map(int, input().split()))

left = [1] * n
right = [1] * n
answer = [0] * n

# 计算 left 数组
for i in range(1, n):
    left[i] = left[i - 1] * nums[i - 1]

# 计算 right 数组
for i in range(n - 2, -1, -1):
    right[i] = right[i + 1] * nums[i + 1]

# 计算答案
for i in range(n):
    answer[i] = left[i] * right[i]

# print(*left)
# print(*right)
print(*answer)
